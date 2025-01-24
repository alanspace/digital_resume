import cv2
import pytesseract
from PIL import Image
import numpy as np

# Load the image
image_path = "your_resume_image.png"  # Replace with your image file path
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to binarize the image
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Noise reduction (optional)
kernel = np.ones((1, 1), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Save preprocessed image (optional for review)
cv2.imwrite("processed_resume.png", binary)

# OCR to extract text
extracted_text = pytesseract.image_to_string(binary)

# Print extracted text
print(extracted_text)

# Optionally, save extracted text to a file
with open("resume_text.txt", "w") as file:
    file.write(extracted_text)

import re

# Load extracted text from file
with open("resume_text.txt", "r") as file:
    text = file.read()

# Example: Extracting sections using regex
name = re.search(r"(Matthew Jones)", text)
profile = re.search(r"Profile(.*?)(?=Employment History)", text, re.DOTALL)
employment_history = re.search(r"Employment History(.*?)(?=Education)", text, re.DOTALL)

print("Name:", name.group(1) if name else "Not Found")
print("Profile Summary:", profile.group(1).strip() if profile else "Not Found")
print("Employment History:", employment_history.group(1).strip() if employment_history else "Not Found")