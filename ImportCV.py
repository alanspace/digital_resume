import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text")  # Extract text
    return text

# Provide your PDF file path
pdf_path = "Shek_Lun_leung,_Alan_Resume.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

# Save extracted text to a file
with open("resume_text.txt", "w") as file:
    file.write(extracted_text)

print("Extracted Text:\n", extracted_text)

# from pdf2image import convert_from_path
# import pytesseract
# import cv2
# import numpy as np

# def ocr_from_pdf(pdf_path):
#     # Convert PDF to images
#     pages = convert_from_path(pdf_path, 300)  # 300 DPI for better accuracy
#     extracted_text = ""

#     for i, page in enumerate(pages):
#         # Convert page to OpenCV image
#         page_cv = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

#         # Convert to grayscale
#         gray = cv2.cvtColor(page_cv, cv2.COLOR_BGR2GRAY)

#         # Apply thresholding
#         binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#         # OCR extraction
#         text = pytesseract.image_to_string(binary)

#         extracted_text += f"\n\n--- Page {i+1} ---\n{text}"

#     return extracted_text

# # Provide your PDF file path
# pdf_path = "your_resume.pdf"
# extracted_text = ocr_from_pdf(pdf_path)

# # Save to text file
# with open("resume_text.txt", "w") as file:
#     file.write(extracted_text)

# print("OCR Extracted Text:\n", extracted_text)


# def preprocess_image(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
#     blurred = cv2.medianBlur(gray, 3)  # Reduce noise
#     binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#     return binary

import re

# Load extracted text
with open("resume_text.txt", "r") as file:
    text = file.read()

# Example: Extracting key sections
name = re.search(r"(\b[A-Z][a-z]+ [A-Z][a-z]+\b)", text)  # Matches full name pattern
experience = re.search(r"(?i)employment history(.*?)(?=education)", text, re.DOTALL)

print("Name:", name.group(1) if name else "Not Found")
print("Experience Section:\n", experience.group(1).strip() if experience else "Not Found")