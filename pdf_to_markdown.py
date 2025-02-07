import os
import PyPDF2
import re
from pathlib import Path

def convert_pdf_to_markdown(pdf_path, output_dir=None):
    """
    Convert PDF to markdown format with proper formatting for LLM consumption
    
    Args:
        pdf_path (str): Path to input PDF file
        output_dir (str, optional): Directory to save markdown file. Defaults to same directory as PDF.
    """
    # Open PDF file
    with open(pdf_path, 'rb') as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n\n"
            
        # Clean up text
        # Remove multiple newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        # Remove trailing/leading whitespace
        text = text.strip()
        
        # Format as markdown
        markdown_text = f"""# {Path(pdf_path).stem}

{text}
"""
        
        # Determine output path
        if output_dir:
            output_path = Path(output_dir) / f"{Path(pdf_path).stem}.md"
        else:
            output_path = Path(pdf_path).with_suffix('.md')
            
        # Save markdown file
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_text)
            
        print(f"Converted {pdf_path} to {output_path}")

def main():
    # Get input PDF path
    pdf_path = input("Enter path to PDF file: ")
    
    # Get optional output directory
    output_dir = input("Enter output directory (press Enter to use same directory as PDF): ").strip()
    if not output_dir:
        output_dir = None
        
    # Convert PDF to markdown
    convert_pdf_to_markdown(pdf_path, output_dir)

if __name__ == "__main__":
    main() 