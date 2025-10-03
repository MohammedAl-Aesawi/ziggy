import os
import streamlit as st
from openai import OpenAI

# openai api
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"]) 

st.set_page_config(page_title="Ziggy AI", page_icon="🚀")
st.title("🚀 Ziggy AI: Your Startup Mentor")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Ziggy AI, a startup mentor."}
    ]

for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])


if prompt := st.chat_input("Ask Ziggy about your startup idea..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    try:

        response = client.responses.create(
            model= "gpt-4o-mini",
            input=st.session_state.messages
        )
        bot_reply = response.output[0].content[0].text

        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    except Exception as e:
        st.error(f"Error: {e}")
