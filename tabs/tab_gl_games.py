"""Tab 17: GL Games - Developmental activity cards + games coach chat."""
import streamlit as st
from utils.state import gl_age
from prompts.gl_games import GL_GAMES_PROMPT


ACTIVITIES = [
    {
        "name": "Peek-a-Boo Variations",
        "category": "Cognitive",
        "items": "blanket, cup",
        "steps": [
            "Hide face behind hands",
            "Hide toy under blanket",
            "Hide toy under cup - watch GL look for it",
        ],
        "watch": "Does GL look for the hidden object?",
    },
    {
        "name": "Texture Safari",
        "category": "Sensory",
        "items": "towel, sponge, wooden spoon, cold spoon, warm cloth",
        "steps": [
            "Let GL touch each texture",
            "Name it: smooth, rough, soft, cold, warm",
            "Watch which ones GL reaches for again",
        ],
        "watch": "Does GL show preference?",
    },
    {
        "name": "Drop and Watch",
        "category": "Cognitive",
        "items": "spoon, rattle",
        "steps": [
            "Give GL a spoon",
            "He drops it - pick it up",
            "Repeat - he's learning HE causes things to happen",
        ],
        "watch": "Does GL drop on purpose and look down?",
    },
    {
        "name": "Mirror Face",
        "category": "Social",
        "items": "mirror",
        "steps": [
            "Sit with GL in front of mirror",
            "Make exaggerated faces",
            "Point to mirror-GL: \"Who's that? That's Gian Lucca!\"",
        ],
        "watch": "Does GL smile at his reflection?",
    },
    {
        "name": "Container Play",
        "category": "Motor",
        "items": "plastic containers, small toys",
        "steps": [
            "Show GL how to put toys IN container",
            "Dump them out",
            "Let GL try",
        ],
        "watch": "Does GL try to put objects in?",
    },
    {
        "name": "Clap Along",
        "category": "Language",
        "items": "none",
        "steps": [
            "Clap a simple rhythm",
            "Sing while clapping",
            "Help GL clap by holding his hands",
        ],
        "watch": "Does GL try to clap independently?",
    },
    {
        "name": "Tummy Roll",
        "category": "Motor",
        "items": "rolled towel",
        "steps": [
            "Place rolled towel under GL's chest",
            "Put toy just out of reach",
            "Encourage reaching",
        ],
        "watch": "Does GL shift weight to reach?",
    },
    {
        "name": "Sound Shaker",
        "category": "Sensory",
        "items": "water bottle with rice, keys",
        "steps": [
            "Shake bottle near GL's left ear, then right",
            "Let GL shake it",
            "Try different sounds",
        ],
        "watch": "Does GL turn toward sound?",
    },
    {
        "name": "Book Flip",
        "category": "Language",
        "items": "board book",
        "steps": [
            "Open book, point at pictures",
            "Name each picture",
            "Let GL grab and flip pages",
        ],
        "watch": "Does GL babble while looking at pictures?",
    },
    {
        "name": "Reach and Roll",
        "category": "Motor",
        "items": "ball",
        "steps": [
            "Sit GL up supported",
            "Roll ball slowly toward GL",
            "Encourage GL to reach and grab",
        ],
        "watch": "Does GL reach with both hands?",
    },
]

GAME_CATEGORIES = ["All", "Sensory", "Motor", "Cognitive", "Social", "Language"]

CATEGORY_EMOJI = {
    "Sensory": "🖐️",
    "Motor": "💪",
    "Cognitive": "🧠",
    "Social": "👶",
    "Language": "🗣️",
}


def render():
    st.header("GL Games")
    age = gl_age()
    st.caption(f"Developmental activities for GL. Age: {age['months']:.1f} months ({age['days']} days).")

    # Category filter
    selected_cat = st.radio(
        "Filter by category",
        GAME_CATEGORIES,
        horizontal=True,
    )

    # Filter activities
    if selected_cat == "All":
        filtered = ACTIVITIES
    else:
        filtered = [a for a in ACTIVITIES if a["category"] == selected_cat]

    # Activity cards in 2 columns
    cols = st.columns(2)
    for i, activity in enumerate(filtered):
        with cols[i % 2]:
            with st.container(border=True):
                emoji = CATEGORY_EMOJI.get(activity["category"], "")
                st.markdown(f"### {emoji} {activity['name']}")
                st.markdown(f"**Category:** {activity['category']}")
                st.markdown(f"**Items needed:** {activity['items']}")
                st.markdown("**Steps:**")
                for j, step in enumerate(activity["steps"], 1):
                    st.markdown(f"{j}. {step}")
                st.markdown(f"**Watch for:** {activity['watch']}")
                checked = st.checkbox(
                    "We played this!",
                    value=activity["name"] in st.session_state.gl_games_done,
                    key=f"game_{activity['name']}",
                )
                if checked and activity["name"] not in st.session_state.gl_games_done:
                    st.session_state.gl_games_done.append(activity["name"])
                elif not checked and activity["name"] in st.session_state.gl_games_done:
                    st.session_state.gl_games_done.remove(activity["name"])

    played_count = len(st.session_state.gl_games_done)
    st.success(f"Played **{played_count} of {len(ACTIVITIES)}** activities")

    st.divider()

    # Chat section
    with st.expander("Ask Games Coach"):
        for msg in st.session_state.gl_games_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        col1, col2 = st.columns([5, 1])
        with col1:
            user_msg = st.text_input(
                "Ask about games...",
                key="gl_games_chat_input",
                label_visibility="collapsed",
            )
        with col2:
            if st.button("Send", key="gl_games_send"):
                if user_msg:
                    st.session_state.gl_games_messages.append({"role": "user", "content": user_msg})
                    st.rerun()

        if st.session_state.gl_games_messages and st.session_state.gl_games_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        from utils.ai_client import chat
                        reply = chat(GL_GAMES_PROMPT, st.session_state.gl_games_messages)
                        st.markdown(reply)
                        st.session_state.gl_games_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")
