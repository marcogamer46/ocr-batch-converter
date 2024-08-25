import os
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Set Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Print Tesseract version for debugging
print("Tesseract version:", pytesseract.get_tesseract_version())

def convert_image_to_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")
        return None

def batch_convert(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                input_path = os.path.join(input_folder, filename)
                
                print(f"Processing: {filename}")
                text = convert_image_to_text(input_path)
                
                if text:
                    out_file.write(f"--- {filename} ---\n")
                    out_file.write(text)
                    out_file.write("\n\n")
                    print(f"Text from {filename} added to output file")
                else:
                    print(f"Failed to extract text from: {filename}")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select Input Folder")
    return folder_path

def select_output_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt")],
                                             title="Save Output As")
    return file_path

if __name__ == "__main__":
    print("Select the input folder containing your images.")
    input_folder = select_folder()
    
    if not input_folder:
        print("No folder selected. Exiting.")
        exit()
    
    print("Select where to save the output text file.")
    output_file = select_output_file()
    
    if not output_file:
        print("No output file selected. Exiting.")
        exit()
    
    print(f"Input folder: {input_folder}")
    print(f"Output file: {output_file}")
    
    batch_convert(input_folder, output_file)
    print("Batch conversion complete. All text saved to:", output_file)