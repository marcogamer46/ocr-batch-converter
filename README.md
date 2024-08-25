```markdown
# Image to Text Converter

This Python script converts images to text using Optical Character Recognition (OCR) technology. It processes multiple image files in a selected folder and saves the extracted text to a single output file.

## Features

- Batch processing of images
- Supports multiple image formats (PNG, JPG, JPEG, TIFF, BMP)
- User-friendly folder and file selection using GUI dialogs
- Outputs all extracted text to a single file with clear separation between images

## Requirements

- Python 3.x
- Tesseract OCR
- Python libraries: 
  - pytesseract
  - Pillow (PIL)
  - tkinter (usually comes with Python)

## Installation

1. Install Tesseract OCR:
   - Windows: Download and install from [GitHub Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - macOS: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`

2. Install required Python libraries:
   ```
   pip install pytesseract Pillow
   ```

3. Update the Tesseract command path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
   Adjust this path according to your Tesseract installation.

## Usage

1. Run the script:
   ```
   python image_to_text.py
   ```

2. When prompted, select the input folder containing your images.

3. Choose a location and name for the output text file.

4. The script will process all supported image files in the selected folder and save the extracted text to the output file.

## Output

The script generates a single text file containing the extracted text from all processed images. Each image's text is preceded by the filename and separated by newlines for easy reading.

## Troubleshooting

- Ensure Tesseract is correctly installed and the path in the script is correct.
- Check the console output for any error messages during processing.
- Verify that your images are in a supported format and are readable.


## License

[MIT](https://choosealicense.com/licenses/mit/)
```

This README provides a comprehensive guide on how to set up and use the image-to-text conversion script. It includes information on installation, usage, requirements, and troubleshooting. You may want to customize the "Contributing" and "License" sections according to your preferences and the actual license you choose for your project.
