
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

st.title("Ask Buddy - AI QnA Bot")
st.markdown("My QnA bot with LangChain and Google Gemini!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

# Accept user input
query = st.chat_input("Ask anything?")

if query:
    # Display and save the user's message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })
    st.chat_message("user").markdown(query)

    # Get Gemini's response
    res = llm.invoke(query)
    answer = res.content

    # Extract text if the response contains content blocks
    if isinstance(answer, list):
        answer = "\n".join(
            block["text"]
            for block in answer
            if isinstance(block, dict) and block.get("type") == "text"
        )

    # Display and save the assistant's response
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
