"""Tab 19: GL Music - Music development playlist, activities, reaction log + chat."""
import streamlit as st
from utils.state import gl_age
from prompts.gl_music import GL_MUSIC_PROMPT


PLAYLIST = [
    ("James Harcourt", "Aesthesis", "GL's anthem"),
    ("Nils Frahm", "Says", "Minimal piano, builds prediction"),
    ("Bonobo", "Kerala", "Organic electronic, tempo changes"),
    ("Kiasmos", "Blurred", "Subtle rhythms, hypnotic"),
    ("Olafur Arnalds", "Near Light", "Strings + electronics, emotional"),
]

MUSIC_ACTIVITIES = [
    {
        "name": "The Drop Game",
        "description": (
            "Play a song, pause right before the build/drop. "
            "Watch GL's face for anticipation. Resume. That's prediction forming."
        ),
    },
    {
        "name": "Echo Crow",
        "description": (
            "GL crows. Peter crows back in rhythm. Add a clap. "
            "Now it's call-and-response percussion."
        ),
    },
    {
        "name": "Tempo Walk",
        "description": (
            "Carry GL around. Walk slow to slow music, fast to fast. "
            "Body learns tempo before ears."
        ),
    },
    {
        "name": "Drum Circle",
        "description": (
            "Pots, spoons, tupperware. Tap a rhythm. Let GL bang. "
            "Celebrate every hit."
        ),
    },
    {
        "name": "Lullaby DJ Set",
        "description": (
            "Play a 15-min set: start upbeat, gradually slow tempo, "
            "end with ambient. Teaches GL that music = sleep cue."
        ),
    },
]


def render():
    st.header("GL Music Lab")
    age = gl_age()
    st.caption(f"Music development for GL. Age: {age['months']:.1f} months ({age['days']} days).")

    # This Week's Playlist
    st.subheader("This Week's Playlist")
    for artist, track, note in PLAYLIST:
        search_query = f"{artist} {track}".replace(" ", "%20")
        spotify_url = f"https://open.spotify.com/search/{search_query}"
        st.markdown(
            f"- **{artist}** - {track} &nbsp; "
            f"[{chr(9654)} Spotify]({spotify_url}) &nbsp; *{note}*"
        )

    st.divider()

    # Activity Cards
    st.subheader("Music Activities")
    cols = st.columns(2)
    for i, activity in enumerate(MUSIC_ACTIVITIES):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### {activity['name']}")
                st.markdown(activity["description"])

    st.divider()

    # GL's Reactions log
    st.subheader("GL's Reactions")
    st.caption("Log what GL does when he hears music. Build his profile.")

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        new_reaction = st.text_input(
            "What did GL do?",
            key="gl_music_reaction_input",
            placeholder="e.g. GL bounced his legs during Aesthesis...",
            label_visibility="collapsed",
        )
    with col_btn:
        if st.button("Save", key="gl_music_reaction_save"):
            if new_reaction:
                from datetime import datetime
                entry = f"[{datetime.now().strftime('%m/%d %I:%M%p')}] {new_reaction}"
                st.session_state.gl_music_reactions.append(entry)
                st.rerun()

    if st.session_state.gl_music_reactions:
        st.markdown("**Recent reactions:**")
        for reaction in reversed(st.session_state.gl_music_reactions[-10:]):
            st.markdown(f"- {reaction}")
    else:
        st.info("No reactions logged yet. Play some music and note what GL does!")

    st.divider()

    # Chat section
    with st.expander("Ask Music Lab"):
        for msg in st.session_state.gl_music_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        col1, col2 = st.columns([5, 1])
        with col1:
            user_msg = st.text_input(
                "Ask about music development...",
                key="gl_music_chat_input",
                label_visibility="collapsed",
            )
        with col2:
            if st.button("Send", key="gl_music_send"):
                if user_msg:
                    st.session_state.gl_music_messages.append({"role": "user", "content": user_msg})
                    st.rerun()

        if st.session_state.gl_music_messages and st.session_state.gl_music_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        from utils.ai_client import chat
                        reply = chat(GL_MUSIC_PROMPT, st.session_state.gl_music_messages)
                        st.markdown(reply)
                        st.session_state.gl_music_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")
