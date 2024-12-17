# anonymize-exam

This project provides a simple Python script to redact sensitive information from a PDF file. The script uses the `PyMuPDF` library to add redaction annotations to specific areas of a PDF page, then applies the redactions and removes metadata from the document.

## Features

- Redacts specific areas on the pages of a PDF document.
- Removes metadata from the document to protect sensitive information.
- Outputs the redacted PDF to a new file.

## Requirements

This project has the following dependencies:

- Python 3.6 or higher.
- `PyMuPDF` library.

All required packages are listed in the `requirements.txt` file. To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Interface

The script is designed to be used from the command line. The syntax is:

```bash
python redact_pdf.py <source_pdf> <destination_pdf>
```

Where:
- `<source_pdf>` is the path to the PDF file you want to redact.
- `<destination_pdf>` is the path where the redacted PDF will be saved.

For example:

```bash
python redact_pdf.py input.pdf output_redacted.pdf
```

## Customization

- **Redaction Areas**: You can modify the redaction areas in the `add_redactions()` function. It currently redacts specific regions (left, right, top, and bottom sections) but can be customized to redact other parts of the page as needed.
  
- **Metadata**: The script clears the metadata by calling `doc.set_metadata({})` and `doc.del_xml_metadata()`. You can choose to modify or skip this step if you don't need to remove metadata.

## Troubleshooting

- **Missing PyMuPDF Library**: If you encounter an error related to missing libraries, make sure you have installed the dependencies using `pip install -r requirements.txt`.
  
- **Permission Issues**: Ensure you have read and write permissions for both the source and destination file paths.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify and enhance this tool according to your needs. If you have any issues or suggestions, feel free to open an issue on the project's GitHub page!

---

### `requirements.txt`

To ensure the proper environment setup, the following libraries are required:

```txt
pymupdf
```

