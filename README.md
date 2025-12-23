📄 AI-Powered Resume Analyzer & CSV Generator
An automated pipeline designed for HR teams and recruiters to process bulk resumes efficiently. This tool accepts a ZIP file containing multiple resumes, extracts key information using Google Gemini 2.0 Flash and LangChain, and generates a structured CSV file for easy filtering and analysis.
🚀 Overview
Recruiters often deal with hundreds of resumes in varied formats. Manually extracting data is slow and inconsistent. This project automates the understanding of unstructured PDF data and converts it into a clean, structured tabular format.
Key Features:
Bulk Processing: Upload a single ZIP file containing multiple PDF resumes.
AI-Driven Extraction: Leverages Gemini 2.0 Flash for high-speed, accurate context understanding.
Structured Output: Uses LangChain's with_structured_output and TypedDict to ensure consistent data (no missing columns).
Interactive UI: A clean, user-friendly interface built with Streamlit.
Instant Export: Download the final analysis as a CSV file.
🛠️ Tech Stack
LLM: Google Gemini 2.0 Flash
Orchestration: LangChain
PDF Parsing: PyMuPDF (fitz)
Frontend: Streamlit
Data Handling: Pandas & Python-Dotenv
Schema Validation: Python TypedDict
📋 Extracted Fields
The system extracts the following details from every resume:
Full Name
Email Address
Phone Number
Location
Total Years of Experience
Top Skills (as a list)
Education Level
Brief Professional Summary
⚙️ Installation & Setup
Clone the repository:
code
Bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
Install dependencies:
code
Bash
pip install -r requirements.txt
Set up Environment Variables:
Create a .env file in the root directory and add your Google API Key:
code
Env
GOOGLE_API_KEY=your_gemini_api_key_here
Run the Application:
code
Bash
streamlit run app.py
📂 Project Structure
code
Text
.
├── app.py              # Main Streamlit application
├── .env                # API Key storage (private)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation