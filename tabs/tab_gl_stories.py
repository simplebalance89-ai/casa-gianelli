"""Tab 14: GL Story Buddy - Interactive storytelling for Gian Lucca."""
import streamlit as st
from utils.ai_client import chat
from prompts.gl_story_buddy import GL_SB_PROMPT


def render():
    st.header("GL Story Buddy")
    st.caption("Interactive storytelling starring Gian Lucca. Pick a mode, start a story.")

    if not st.session_state.gl_sb_started:
        st.subheader("Pick a story mode")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("GIAN LUCCA\n(Baby Mode)", use_container_width=True):
                st.session_state.gl_sb_messages = [
                    {"role": "user", "content": "Tell a gentle bedtime story starring baby Gian Lucca (GL). He's a baby, so make it sensory: soft textures, warm sounds, gentle adventures. Keep it soothing and sweet."}
                ]
                st.session_state.gl_sb_started = True
                st.rerun()

        with col2:
            if st.button("BIG KID GL", use_container_width=True):
                st.session_state.gl_sb_messages = [
                    {"role": "user", "content": "Tell a story where Gian Lucca is a big kid (age 5). He's brave, curious, and loves exploring. Give him a fun adventure with choices!"}
                ]
                st.session_state.gl_sb_started = True
                st.rerun()

        with col3:
            if st.button("WHOLE CREW", use_container_width=True):
                st.session_state.gl_sb_messages = [
                    {"role": "user", "content": "Tell a story starring the whole crew: baby GL, his cousins Liam (4, loves Cars) and Logan (3, loves Spider-Man), Daddy Peter (DJ/music), Mommy Gladys (beautiful and strong), Uncle Jimmy and Aunt Jenna. A family adventure!"}
                ]
                st.session_state.gl_sb_started = True
                st.rerun()

        with col4:
            if st.button("DEMO", use_container_width=True):
                st.session_state.gl_sb_messages = [
                    {"role": "user", "content": "Give a quick demo of how GL Story Buddy works. Show a short sample story opening with choices, so the parent can see the format."}
                ]
                st.session_state.gl_sb_started = True
                st.rerun()

        st.info("Pick a mode above to start a new story!")

    else:
        # New Story reset button
        if st.button("New Story"):
            st.session_state.gl_sb_messages = []
            st.session_state.gl_sb_started = False
            st.rerun()

        # Display chat messages
        for msg in st.session_state.gl_sb_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Generate response if last message is from user
        if st.session_state.gl_sb_messages and st.session_state.gl_sb_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Crafting the story..."):
                    try:
                        reply = chat(GL_SB_PROMPT, st.session_state.gl_sb_messages, max_tokens=800)
                        st.markdown(reply)
                        st.session_state.gl_sb_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Connection error: {e}")

        # Chat input for continuing the story
        if user_input := st.chat_input("What happens next?", key="gl_sb_chat_input"):
            st.session_state.gl_sb_messages.append({"role": "user", "content": user_input})
            st.rerun()
