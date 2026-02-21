"""Tab 16: GL Signs - Baby sign language tracker. The showcase tab."""
import streamlit as st
from utils.state import gl_age
from utils.sign_data import BABY_SIGNS, CATEGORIES
from prompts.gl_signs import GL_SIGNS_PROMPT


def render():
    st.header("GL Signs")
    age = gl_age()
    st.caption(f"Baby sign language tracker. GL is {age['months']:.1f} months old ({age['days']} days).")

    # Progress
    total_signs = len(BABY_SIGNS)
    learned = len(st.session_state.gl_signs_learned)
    st.progress(learned / total_signs, text=f"GL knows **{learned} of {total_signs}** signs")

    # Category filter
    selected_cat = st.radio(
        "Filter by category",
        list(CATEGORIES.keys()),
        horizontal=True,
    )
    filter_cat = CATEGORIES[selected_cat]

    # Filter and sort signs
    filtered_signs = []
    for name, data in BABY_SIGNS.items():
        if filter_cat is None or data["category"] == filter_cat:
            filtered_signs.append((name, data))
    filtered_signs.sort(key=lambda x: x[1]["priority"])

    # Sign cards in 3-column grid
    cols = st.columns(3)
    for i, (name, data) in enumerate(filtered_signs):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"<div style='font-size:2.5em;text-align:center'>{data['emoji']}</div>", unsafe_allow_html=True)
                st.markdown(f"### {name}")
                st.markdown(f"**How:** {data['how']}")
                st.markdown(f"**Visual:** {data['visual']}")
                st.markdown(f"**When:** {data['when']}")
                checked = st.checkbox(
                    "GL knows this!",
                    value=name in st.session_state.gl_signs_learned,
                    key=f"sign_{name}",
                )
                if checked and name not in st.session_state.gl_signs_learned:
                    st.session_state.gl_signs_learned.append(name)
                elif not checked and name in st.session_state.gl_signs_learned:
                    st.session_state.gl_signs_learned.remove(name)

    st.divider()

    # This Week's Goal
    st.subheader("This Week's Goal")
    all_sorted = sorted(BABY_SIGNS.items(), key=lambda x: x[1]["priority"])
    next_sign = None
    for name, data in all_sorted:
        if name not in st.session_state.gl_signs_learned:
            next_sign = (name, data)
            break

    if next_sign:
        name, data = next_sign
        st.info(f"**This week:** Use **{name}** every time you {data['when'].lower()} GL will start connecting it within 2 weeks.")
    else:
        st.success("GL knows all 18 signs! Amazing work.")

    st.divider()

    # Chat section
    with st.expander("Ask Sign Coach"):
        for msg in st.session_state.gl_signs_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        col1, col2 = st.columns([5, 1])
        with col1:
            user_msg = st.text_input(
                "Ask about signs...",
                key="gl_signs_chat_input",
                label_visibility="collapsed",
            )
        with col2:
            if st.button("Send", key="gl_signs_send"):
                if user_msg:
                    st.session_state.gl_signs_messages.append({"role": "user", "content": user_msg})
                    st.rerun()

        if st.session_state.gl_signs_messages and st.session_state.gl_signs_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        from utils.ai_client import chat
                        reply = chat(GL_SIGNS_PROMPT, st.session_state.gl_signs_messages)
                        st.markdown(reply)
                        st.session_state.gl_signs_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")
