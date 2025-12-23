import streamlit as st
import pandas as pd
import zipfile
import fitz  # PyMuPDF
import os
import io
from typing import List, TypedDict, Optional
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 1. Define Structured Schema
class ResumeData(TypedDict):
    full_name: str
    email: str
    phone_number: str
    location: str
    total_years_experience: str
    top_skills: List[str]
    education: str
    brief_summary: str

# 2. Text Extraction Logic
def extract_text(pdf_bytes):
    text = ""
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# 3. Main Application UI
st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Resume Analyzer & CSV Generator")
st.write("Upload a ZIP file containing PDF resumes to extract structured data.")

uploaded_file = st.file_uploader("Choose a ZIP file", type="zip")

if uploaded_file:
    if not api_key:
        st.error("API Key not found. Please check your .env file.")
    else:
        if st.button("Generate CSV"):
            extracted_results = []
            
            try:
                with zipfile.ZipFile(uploaded_file, 'r') as z:
                    # Filter for valid PDF files
                    filenames = [f for f in z.namelist() if f.lower().endswith('.pdf') and not f.startswith('__')]
                    
                    if not filenames:
                        st.warning("No PDF files found in the archive.")
                    else:
                        # Initialize Model (Gemini 2.0 Flash)
                        llm = ChatGoogleGenerativeAI(
                            model="gemini-2.5-flash", 
                            google_api_key=api_key, 
                            temperature=0
                        )
                        
                        prompt = ChatPromptTemplate.from_messages([
                            ("system", "Extract structured details from the resume text. Use 'N/A' for missing fields."),
                            ("human", "{text}")
                        ])
                        
                        chain = prompt | llm.with_structured_output(ResumeData)
                        
                        progress_bar = st.progress(0)
                        
                        for i, name in enumerate(filenames):
                            with z.open(name) as f:
                                resume_text = extract_text(f.read())
                                
                            try:
                                # Process with LLM
                                response = chain.invoke({"text": resume_text})
                                data = dict(response)
                                data['filename'] = name
                                extracted_results.append(data)
                            except Exception:
                                pass # Skip errors for individual files
                            
                            progress_bar.progress((i + 1) / len(filenames))

                        if extracted_results:
                            df = pd.DataFrame(extracted_results)
                            
                            # Clean up column order
                            cols = ['filename'] + [c for c in df.columns if c != 'filename']
                            df = df[cols]

                            st.success(f"Processed {len(extracted_results)} resumes.")
                            st.dataframe(df, use_container_width=True)

                            # CSV Download link
                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="Download Results as CSV",
                                data=csv,
                                file_name="resume_data.csv",
                                mime="text/csv"
                            )
            except Exception as e:
                st.error(f"An error occurred: {e}")