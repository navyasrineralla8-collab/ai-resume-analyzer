import streamlit as st
import PyPDF2
from skills import SKILLS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def extract_text(pdf_file):
    text=""
    reader=PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text
    return text.lower()
def find_skills(text):
    found=[]
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found
def get_similarity(resume,job):
    texts=[resume,job]
    cv=CountVectorizer()
    matrix=cv.fit_transform(texts)
    similarity=cosine_similarity(matrix)[0][1]
    return round(similarity*100,2)
st.title("AI resume Analyzer")
uploaded_file=st.file_uploader("upload resume pdf",type="pdf")
job_description=st.text_area("paste job description")
if st.button("Analyze"):
    if uploaded_file and job_description:
        resume_text=extract_text(uploaded_file)
        skills=find_skills(resume_text)
        score=get_similarity(resume_text,job_description.lower())
        job_skills=find-skills(job_description.lower())
        missing=[]
        for skill in job_skills:
            if skill not in skills:
                missing.append(skill)
        st.subheader("match percentage")
        st.write(f"{score}%")
        st.subheader("Skills found")
        st.write(skills)
        st.subheader("missing skills")
        st.write(missing)
    else:
        st.warning("please uploat a resume and enter a job discription")


