"""Tab 13: Story Buddy - Interactive storytelling for Liam & Logan."""
import streamlit as st
from utils.ai_client import chat
from prompts.story_buddy import SB_SYSTEM_PROMPT


def render():
    st.header("Story Buddy")
    st.caption("Interactive storytelling for Liam & Logan. Pick a mode, start a story.")

    if not st.session_state.sb_started:
        st.subheader("Who's story time for?")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Liam", use_container_width=True):
                st.session_state.sb_messages = [
                    {"role": "user", "content": "Tell a story for Liam (age 4). He loves Lightning McQueen, Cars, and SpongeBob. Make it exciting!"}
                ]
                st.session_state.sb_started = True
                st.rerun()

        with col2:
            if st.button("Logan", use_container_width=True):
                st.session_state.sb_messages = [
                    {"role": "user", "content": "Tell a story for Logan (age 3). He loves Spider-Man and Miles Morales. Make it adventurous but not too scary!"}
                ]
                st.session_state.sb_started = True
                st.rerun()

        with col3:
            if st.button("Both Boys", use_container_width=True):
                st.session_state.sb_messages = [
                    {"role": "user", "content": "Tell a story for both Liam (4) and Logan (3) together. Liam loves Cars and SpongeBob, Logan loves Spider-Man. Make them both heroes!"}
                ]
                st.session_state.sb_started = True
                st.rerun()

        with col4:
            if st.button("Demo Mode", use_container_width=True):
                st.session_state.sb_messages = [
                    {"role": "user", "content": "Give a quick demo of how Story Buddy works. Show a short sample story opening with choices, so the parent can see the format."}
                ]
                st.session_state.sb_started = True
                st.rerun()

        st.info("Pick a mode above to start a new story!")

    else:
        # New Story reset button
        if st.button("New Story"):
            st.session_state.sb_messages = []
            st.session_state.sb_started = False
            st.rerun()

        # Display chat messages
        for msg in st.session_state.sb_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Generate response if last message is from user
        if st.session_state.sb_messages and st.session_state.sb_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Crafting the story..."):
                    try:
                        reply = chat(SB_SYSTEM_PROMPT, st.session_state.sb_messages, max_tokens=800)
                        st.markdown(reply)
                        st.session_state.sb_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Connection error: {e}")

        # Chat input for continuing the story
        if user_input := st.chat_input("What happens next?", key="sb_chat_input"):
            st.session_state.sb_messages.append({"role": "user", "content": user_input})
            st.rerun()
