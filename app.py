import streamlit as st
from groq import Groq                                          
st.set_page_config(page_title='AI_Interview_Assistant', page_icon='🎃', layout='centered')
st.title('AI_Interview_Assistant')
st.caption('practice and perpare for your palcement here')

try:
  client = Groq(api_key = ["GROQ_API_KEY"])

except(KeyError, FileNotFound):
  st.error("API Key is missing.Add it in Advanced Setting")
  st.stop()

role = st.selectbox('Job Title', ['Machine Learning Engineer','Senior Software engineer','Devops Engineer','Data Analyst','Prompt Engineer','other'])
