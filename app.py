import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyBDPoqkFJIDIv0QcCi5MHA8WRv3nCI5imc")
model = genai.GenerativeModel("gemini-1.5-pro")
st.title("AI Assistant")
st.subheader("Enter your query below:")
user_input = st.text_input("Write your query here:")
if user_input:
    prompt = f"You are a helpful assistant. Answer the following user query clearly and accurately:\n\n{user_input}"
    response = model.generate_content(prompt)
    st.write(response.text)
 