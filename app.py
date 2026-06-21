import streamlit as st

from src.query import ask_question

st.set_page_config(
    page_title="Document Q&A Bot",
    layout="wide"
)

st.title("📚 My Q&A ChatBot")

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input(
    "Ask a question"
)

if st.button("Submit"):

    if question:

        with st.spinner(
                "Searching documents..."
        ):

            answer = ask_question(
                question
            )

            st.session_state.history.append(
                (question, answer)
            )

for q, a in reversed(
        st.session_state.history
):

    st.markdown(
        f"### Question\n{q}"
    )

    st.markdown(
        f"### Answer\n{a}"
    )

    st.divider()