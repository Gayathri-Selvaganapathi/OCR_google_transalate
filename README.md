# Optical Character Recognition (OCR) Project

## Overview

This project aims to provide Optical Character Recognition (OCR) capabilities to users, allowing them to upload an image containing text and extract the characters or text from it. Additionally, it offers the functionality for users to choose the preferred area of the uploaded image to perform OCR, providing flexibility and accuracy.

## Features

1. **Image Upload**: Users can upload an image containing text.
2. **Select Preferred Area**: Users have the option to select the area of the uploaded image from which they want to extract text.
3. **Text Extraction**: The system processes the uploaded image and extracts the text using OCR algorithms.
4. **Output Display**: The extracted text is displayed to the user for review or further processing.

## Getting Started

## Initial Requirements
Install the below requirments
1. Anaconda: Donwload Link (https://www.anaconda.com/download/success)
2. Python: Download Link (https://www.python.org/downloads/)
3. Tessaract: Download Link 
(For windows: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
Other OS: https://tesseract-ocr.github.io/tessdoc/Compiling.html)

## Edit Environment Variable path

For Windows machine, after Installing the Python and Tessaract edit the enviroment varaible and include the python and tessaract application paths to the sytem variable.
 

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Create the environment

```bash
conda env create -f environment.yml
```

3. Activate the environment 

```bash
conda activate env_ocr  
```

4. Updatin the activated Environment

```bash
conda env update -f environment.yml --prune
```

5. Run the application by executing the below command.

```bash
streamlit run app.py
```

5. Access the application through the web browser at `http://localhost:8501`.

## Usage

1. **Upload Image**: Click on the upload button and select an image file containing text.
2. **Select Preferred Area**: If desired, use the bounding to select the preferred area of the uploaded image.
3. **Extract Text**: Click on the "Convert Text" button to initiate the OCR process.
4. **View Output**: The extracted text will be displayed on the screen.

## Technologies Used

- **Python**: The primary programming language used for backend development.
- **Streamlit**: A lightweight web framework used for building the web application.
- **pytesseract**: An OCR engine used for recognizing text within images.
- **GoogleTranslate**: A free and unlimited python library used to translate the text to deseired Languages.

## Google Transalate Supported Languages

https://py-googletrans.readthedocs.io/en/latest/

## Tessaract Supported Languages

https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Special thanks to the developers of Streamlit and Tesseract for their excellent libraries and documentation.
- This project was inspired by the need for easy-to-use OCR tools for various applications.