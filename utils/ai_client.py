"""Shared Azure OpenAI client for Casa Gianelli."""
import os
import streamlit as st
from openai import AzureOpenAI

AZURE_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
AZURE_KEY = os.environ.get("AZURE_OPENAI_KEY", "")
AZURE_MODEL = os.environ.get("AZURE_OPENAI_MODEL", "gpt-4o")


def get_client():
    return AzureOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_KEY,
        api_version="2024-12-01-preview"
    )


def chat(system_prompt, messages, temperature=0.85, max_tokens=500):
    """Send chat to Azure OpenAI and return response text."""
    client = get_client()
    model = AZURE_MODEL
    api_messages = [{"role": "system", "content": system_prompt}]
    api_messages.extend(messages)
    response = client.chat.completions.create(
        model=model,
        messages=api_messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


def render_chat(state_key, system_prompt, placeholder="Type a message...", input_key=None, temperature=0.85):
    """Render a chat interface inside an expander. Returns nothing, modifies session_state."""
    if input_key is None:
        input_key = f"{state_key}_input"

    messages = st.session_state[state_key]

    for msg in messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if messages and messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    reply = chat(system_prompt, messages, temperature=temperature)
                    st.markdown(reply)
                    st.session_state[state_key].append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Connection error: {e}")

    if user_input := st.chat_input(placeholder, key=input_key):
        st.session_state[state_key].append({"role": "user", "content": user_input})
        st.rerun()
