import os
import sys
import ocrmypdf


def ocr_pdfs(input_folder, output_folder, language='eng'):
    """
    Process PDF files in the input folder using OCR and save them to the output folder.

    Parameters:
        input_folder (str): Folder containing input PDF files.
        output_folder (str): Folder to save processed PDF files.
        language (str): Language(s) for OCR. Default is 'eng' (English).
                       Combine languages using a '+' (e.g., 'eng+rus').
    """
    # Ensure input and output folders exist
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        sys.exit(1)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in '{input_folder}'.")
        return

    for pdf_file in pdf_files:
        input_path = os.path.join(input_folder, pdf_file)
        output_path = os.path.join(output_folder, pdf_file)

        # Skip processing if the output file already exists
        if os.path.exists(output_path):
            print(f"Skipping '{pdf_file}' - already processed.")
            continue

        print(f"Processing '{pdf_file}'...")

        try:
            ocrmypdf.ocr(
                input_file=input_path,
                output_file=output_path,
                language=language,
                deskew=True,
                force_ocr=True,  # Force OCR even if the PDF has searchable text
                progress_bar=True
            )
            print(f"Saved OCR'd PDF to '{output_path}'.")
        except Exception as e:
            print(f"Failed to OCR '{pdf_file}': {e}")


if __name__ == "__main__":
    # Define the input and output folders
    source_folder = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(source_folder, 'input')
    output_folder = os.path.join(source_folder, 'output')

    # Language documentation
    """
    Available Tesseract language codes:
    - English: 'eng'
    - Slovak: 'slk'
    - Czech: 'ces'
    - Russian: 'rus'
    - Chinese Simplified: 'chi_sim'
    - Chinese Traditional: 'chi_tra'
    - Polish: 'pol'
    - German: 'deu'
    - French: 'fra'

    Combine multiple languages using a '+' (e.g., 'eng+rus').
    """

    # Set the language for OCR (default to English)
    language = 'eng'

    # Allow passing the language as a command-line argument
    if len(sys.argv) > 1:
        language = sys.argv[1]  # e.g., python main.py eng+rus

    # Call the OCR function
    ocr_pdfs(input_folder, output_folder, language)