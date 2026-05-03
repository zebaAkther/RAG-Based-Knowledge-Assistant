import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Enterprise Knowledge Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS (for styling)
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #aaaaaa;
    margin-bottom: 30px;
}
.stTextInput > div > div > input {
    background-color: #1c1f26;
    color: white;
}
.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}
.response-box {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    color: white;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 Enterprise Knowledge Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything about your company data</div>', unsafe_allow_html=True)

# Input
question = st.text_input("🔍 Ask a question")

# Button
if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        try:
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": question},
                headers={"authorization": "admin"}  # ✅ FIXED AUTH
            )

            if response.status_code == 200:
                answer = response.json()["answer"]

                st.markdown(f"""
                <div class="response-box">
                <strong>Answer:</strong><br><br>
                {answer}
                </div>
                """, unsafe_allow_html=True)

            else:
                st.error("❌ Server error. Check backend.")

        except Exception as e:
            st.error("⚠️ Could not connect to backend. Is FastAPI running?")