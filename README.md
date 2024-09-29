# PDF to Audiobook Converter

This project converts PDF documents into audiobooks using **Streamlit** for the web interface and **pyttsx3** for text-to-speech conversion. Users can upload a PDF, select the desired voice (male or female), and generate an audiobook in MP3 format.

## Features

- Upload a PDF file.
- Choose between male or female voice for narration.
- Generate and download the audiobook in MP3 format.

## Installation

To set up and run this project locally, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/pdf-to-audiobook.git
cd pdf-to-audiobook
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Once dependencies are installed, start the Streamlit app by running:

```bash
streamlit run audiobook.py
```

This will open the app in your default browser.

## How to Use

1. **Upload a PDF**: Click the "Browse files" button to upload your PDF document.
2. **Select Voice**: Choose between a male or female voice for the narration.
3. **Generate Audiobook**: Click the "Generate Audiobook" button to convert the PDF text into an MP3 file.
4. **Download the Audiobook**: After conversion, the app will allow you to download the generated MP3 file.

## Project Structure

```bash
pdf-to-audiobook/
├── audiobook.py          # Main Streamlit app script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Dependencies

- **Streamlit**: For building the web app interface.
- **pyttsx3**: For converting text to speech.
- **PyMuPDF** (`fitz`): For extracting text from the uploaded PDF files.

## Known Issues

- PDFs with complex formatting (e.g., images or tables) may not be processed accurately.
- The conversion speed can vary based on the size of the PDF.

## Contributing

Contributions are welcome! If you want to improve this project, please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.








