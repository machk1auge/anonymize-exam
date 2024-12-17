import argparse

import pymupdf


def add_redactions(page, page_width, page_height):
    """Adds redaction annotations to a given page."""
    left_area = pymupdf.Rect(0, 0, 40, page_height)
    right_area = pymupdf.Rect(page_width - 40, 0, page_width, page_height)
    top_area = pymupdf.Rect(0, 0, page_width, 40)
    bottom_left_area = pymupdf.Rect(
        0, page_height - 40, page_width / 2 - 50, page_height
    )
    bottom_right_area = pymupdf.Rect(
        page_width / 2 + 50, page_height - 40, page_width, page_height
    )

    page.add_redact_annot(left_area, fill=(1, 1, 1))
    page.add_redact_annot(right_area, fill=(1, 1, 1))
    page.add_redact_annot(top_area, fill=(1, 1, 1))
    page.add_redact_annot(bottom_left_area, fill=(1, 1, 1))
    page.add_redact_annot(bottom_right_area, fill=(1, 1, 1))


def main():
    # Creating a new argument parser
    parser = argparse.ArgumentParser(description="Redact a PDF document.")

    # Adding arguments for the source PDF file path and destination PDF file path
    parser.add_argument("source", help="Path to the source PDF file.")
    parser.add_argument("destination", help="Path to save the redacted PDF file.")

    # Parsing the arguments provided by the user
    args = parser.parse_args()

    try:
        # Open the PDF document using a context manager
        with pymupdf.open(args.source) as doc:
            # Get the first page as reference
            first_page = doc[0]
            page_width = first_page.rect.width
            page_height = first_page.rect.height

            # Define specific redaction for the first page
            first_page_right_up_corner = pymupdf.Rect(
                page_width - 50, 25, page_width, 60
            )
            first_page.add_redact_annot(first_page_right_up_corner, fill=(1, 1, 1))
            add_redactions(first_page, page_width, page_height)
            first_page.apply_redactions(graphics=0)

            # Loop through the rest of the pages and add redaction annotations
            for page_num in range(1, len(doc)):
                page = doc[page_num]
                add_redactions(page, page_width, page_height)
                page.apply_redactions(graphics=0)

            # Remove all metadata
            doc.set_metadata({})
            doc.del_xml_metadata()

            # Save the modified document
            doc.save(args.destination)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
