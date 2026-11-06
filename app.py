
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Study Assistant")
st.write("Your personal AI-powered learning assistant.")

with st.sidebar:
    st.header("About this project")
    st.write("Built using Python, Streamlit and Gemini AI.")
    st.write("Created for student learning and exam preparation.")

subject = st.selectbox(
    "Choose a subject",
    [
        "Python Programming",
        "Java Programming",
        "Data Structures",
        "Aptitude",
        "Computer Science",
        "Other"
    ]
)

level = st.selectbox(
    "Choose your learning level",
    ["Beginner", "Intermediate", "Exam Preparation"]
)

question = st.text_area(
    "Enter your question",
    placeholder="Example: Explain OOP concepts with examples."
)

if st.button("Generate Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            client = genai.Client(
                api_key=st.secrets["GEMINI_API_KEY"]
            )

            prompt = f"""
            You are an educational AI assistant.
            Subject: {subject}
            Learning level: {level}
            Question: {question}

            Explain the answer in simple language.
            Include examples and important points.
            For exam preparation, use clear headings.
            If uncertain, say so rather than inventing facts.
            """

            with st.spinner("Generating answer..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.subheader("Answer")
            st.markdown(response.text or "No answer returned.")

        except Exception:
            st.error(
                "Unable to generate an answer. "
                "Check the API key, model availability, "
                "and API usage limits."
            )

st.caption(
    "Verify important information with your textbooks "
    and trusted learning resources."
)
