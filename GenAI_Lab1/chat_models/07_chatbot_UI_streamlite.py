import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# 1. Load environment variables
load_dotenv()

# 2. Configure Streamlit Page
st.set_page_config(page_title="DevOps & AI Chatbot", page_icon="🤖")
st.title("🤖 DevOps & AI Expert Chatbot")
st.caption("Ask me anything about DevOps workflows, CI/CD, Cloud, or AI integration.")

# 3. Initialize the Model (Keeping your exact logic)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 4. Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are an expert in Devops and AI ")
    ]

# 5. Display Past Chat Messages (Skipping the system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# 6. Handle User Input
if prompt := st.chat_input("What is on your mind?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Append user message to state
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    # Generate response using your model logic
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
            message_placeholder.markdown(response.content)
            
    # Append assistant response to state
    st.session_state.messages.append(AIMessage(content=response.content))