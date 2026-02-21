"""Tab 18: GL Milestones - Developmental milestone tracker + chat."""
import streamlit as st
from utils.state import gl_age
from prompts.gl_milestones import GL_MILESTONES_PROMPT


MILESTONES = {
    "Motor": [
        ("Rolls both ways", 4, 6),
        ("Sits without support", 6, 8),
        ("Gets to sitting position alone", 8, 9),
        ("Crawls", 7, 10),
        ("Pulls to stand", 8, 10),
        ("Cruises along furniture", 9, 12),
    ],
    "Cognitive": [
        ("Looks for dropped objects", 6, 8),
        ("Explores objects by banging/shaking", 6, 9),
        ("Finds hidden toy (object permanence)", 8, 12),
        ("Understands cause and effect", 7, 10),
    ],
    "Language": [
        ("Babbles consonant chains (ba-ba, da-da)", 6, 8),
        ("Responds to own name", 6, 7),
        ("Understands 'no'", 8, 10),
        ("Points at things", 9, 12),
        ("Says first word with meaning", 10, 14),
    ],
    "Social": [
        ("Stranger anxiety begins", 6, 8),
        ("Plays peekaboo", 6, 9),
        ("Waves bye-bye", 9, 12),
        ("Shows preference for certain people", 7, 10),
    ],
}

CATEGORY_EMOJI = {
    "Motor": "💪",
    "Cognitive": "🧠",
    "Language": "🗣️",
    "Social": "👶",
}


def render():
    st.header("GL Milestones")
    age = gl_age()

    # Big age info box
    st.info(
        f"**Gian Lucca** is **{age['months']:.1f} months** old "
        f"({age['days']} days, {age['weeks']} weeks). "
        f"Day {age['day_1000']} of the First 1000 Days."
    )

    # Progress bar: position on 0-12 month scale
    month_progress = min(age["months"] / 12.0, 1.0)
    st.progress(month_progress, text=f"Month {age['months']:.1f} of 12")

    # Count total and done
    total_milestones = sum(len(v) for v in MILESTONES.values())
    done_count = len(st.session_state.gl_milestones_done)
    st.metric("Milestones Achieved", f"{done_count} / {total_milestones}")

    # Milestone checklist by category
    for category, milestones in MILESTONES.items():
        emoji = CATEGORY_EMOJI.get(category, "")
        with st.expander(f"{emoji} {category} Milestones", expanded=True):
            for name, start_mo, end_mo in milestones:
                label = f"{name} ({start_mo}-{end_mo} mo)"
                checked = st.checkbox(
                    label,
                    value=name in st.session_state.gl_milestones_done,
                    key=f"mile_{name}",
                )
                if checked and name not in st.session_state.gl_milestones_done:
                    st.session_state.gl_milestones_done.append(name)
                elif not checked and name in st.session_state.gl_milestones_done:
                    st.session_state.gl_milestones_done.remove(name)

    st.divider()

    # What's Next section
    st.subheader("What's Next")
    current_months = age["months"]
    upcoming = []
    for category, milestones in MILESTONES.items():
        for name, start_mo, end_mo in milestones:
            if name not in st.session_state.gl_milestones_done:
                # Prioritize milestones whose window includes or is near current age
                distance = max(0, start_mo - current_months)
                upcoming.append((name, category, start_mo, end_mo, distance))

    upcoming.sort(key=lambda x: x[4])
    next_three = upcoming[:3]

    if next_three:
        for name, category, start_mo, end_mo, _ in next_three:
            emoji = CATEGORY_EMOJI.get(category, "")
            if current_months >= start_mo:
                st.warning(f"{emoji} **{name}** - Window: {start_mo}-{end_mo} mo (GL is in this window now)")
            else:
                st.info(f"{emoji} **{name}** - Coming up at {start_mo}-{end_mo} mo")
    else:
        st.success("All milestones achieved! Incredible progress.")

    st.divider()

    # Chat section
    with st.expander("Ask Milestone Tracker"):
        for msg in st.session_state.gl_miles_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        col1, col2 = st.columns([5, 1])
        with col1:
            user_msg = st.text_input(
                "Ask about milestones...",
                key="gl_miles_chat_input",
                label_visibility="collapsed",
            )
        with col2:
            if st.button("Send", key="gl_miles_send"):
                if user_msg:
                    st.session_state.gl_miles_messages.append({"role": "user", "content": user_msg})
                    st.rerun()

        if st.session_state.gl_miles_messages and st.session_state.gl_miles_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        from utils.ai_client import chat
                        reply = chat(GL_MILESTONES_PROMPT, st.session_state.gl_miles_messages)
                        st.markdown(reply)
                        st.session_state.gl_miles_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")
