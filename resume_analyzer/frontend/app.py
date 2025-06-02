import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.utils.job_description_matcher import calculate_similarity
from backend.utils.resume_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and enter a job description to see how well they match.")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste the Job Description Here")

# Analyze button
if st.button("Analyze"):
    if uploaded_file is not None and job_description.strip() != "":
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            similarity = calculate_similarity(resume_text, job_description)
            percentage = round(similarity * 100, 2)
            st.success(f"Similarity Score: {percentage}%")
    else:
        st.error("Please upload a resume and enter a job description.")
