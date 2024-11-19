# OCR PDF Processor

This Python script processes PDF files in a specified input folder, applies Optical Character Recognition (OCR) to them, and saves the processed files to an output folder. The script uses the high-quality ocrmypdf library and supports multiple languages.

## Features

	•	Automatically processes all PDF files in the input folder.
	•	Saves OCR-processed files in the output folder.
	•	Skips already processed files to avoid redundant work.
	•	Supports multiple languages for OCR.
	•	Allows combining multiple languages for enhanced accuracy.

## Requirements

Python Version

	•	Python 3.6 or higher.

## Dependencies

	•	ocrmypdf: Install via pip install ocrmypdf.
	•	Tesseract OCR Engine: Install and ensure it’s added to your system PATH.
	•	Ghostscript: Required for PDF manipulation.
	•	Optional:
	•	pngquant for image optimization.
	•	jbig2enc for advanced JBIG2 compression.

## Installation

1. Install Tesseract

macOS
```bash
brew install tesseract
```

Linux (Debian/Ubuntu)
```bash
sudo apt-get install tesseract-ocr
```

Windows

	•	Download the installer from Tesseract OCR.
	•	Run the installer and add Tesseract to your system PATH.

2. Install Python Dependencies
```bash
pip install ocrmypdf
```

3. Install Ghostscript

macOS
```bash
brew install ghostscript
```
Linux (Debian/Ubuntu)
```bash
sudo apt-get install ghostscript
```
Windows

	•	Download the installer from Ghostscript.
	•	Run the installer and add Ghostscript to your system PATH.

## Usage

	1.	Place PDF files in the input/ folder.
	2.	Run the script:
```bash
python main.py
```

	3.	Processed files will be saved in the output/ folder.

### Language Selection

	•	Default language: English (eng).
	•	To specify a different language, pass it as an argument:
```bash
python main.py slk
```

	•	To combine multiple languages, use +:
```bash
python main.py eng+rus
```

### Folder Structure

OCR/
│
├── main.py        # The Python script
├── input/         # Place your input PDF files here
└── output/        # Processed OCR PDFs will be saved here

### Supported Languages

Language	Code
English	eng
Slovak	slk
Czech	ces
Russian	rus
Chinese Simplified	chi_sim
Chinese Traditional	chi_tra
Polish	pol
German	deu
French	fra

### Combining Languages

Combine multiple languages using a +. For example:
	•	English + Slovak:
```bash
python main.py eng+slk
```

	•	Chinese Simplified + Russian:
```bash
python main.py chi_sim+rus
```
### How It Works

	1.	Input Check: The script scans the input/ folder for PDF files.
	2.	Duplicate Check: Skips processing if the same file already exists in the output/ folder.
	3.	OCR Processing: Applies OCR using the specified language(s).
	4.	Save Output: Saves the processed PDF to the output/ folder.

## Troubleshooting

### Common Issues

	1.	TesseractNotFoundError:
	•	Ensure Tesseract OCR is installed and added to your system PATH.
	2.	Missing Language Data:
	•	Download the required language data (*.traineddata) for Tesseract.
	•	Place the files in Tesseract’s tessdata folder.
	3.	Permission Issues:
	•	Run the command prompt or terminal as an administrator.
