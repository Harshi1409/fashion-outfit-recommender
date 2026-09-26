import streamlit as st

st.title("📚 Exam Preparation Chatbot")

user_input = st.text_input("Ask your question:")

if user_input:
    st.write("### 🤖 Chatbot Response:")
    
    if "ai" in user_input.lower():
        st.write("AI stands for Artificial Intelligence. It helps machines learn and solve problems.")
    elif "python" in user_input.lower():
        st.write("Python is a programming language used for web development, AI, and data science.")
    else:
        st.write("This is a sample answer for exam preparation.")