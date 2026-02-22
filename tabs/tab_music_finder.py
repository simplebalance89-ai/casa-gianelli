"""Simple Balance Music Finder — DJ assistant for Peter."""
import streamlit as st
from utils.ai_client import render_chat

SYSTEM_PROMPT = """You are the Simple Balance Music Finder, Peter's personal DJ assistant. You help with:
- Track discovery by BPM, key, genre, mood, or energy level
- Set building and flow analysis (BPM progression, harmonic mixing via Camelot wheel)
- Genre/mood/functional tagging for tracks
- Identifying tracks from descriptions ("that deep house track with the vocal chop...")
- Finding similar artists and tracks based on Peter's taste

Peter's taste profile:
- Core genres: Melodic house/techno, deep house, progressive, Afterlife-style, controlled chaos
- Key artists: Brunello, Colyn, Tim Engelhardt, Glowal, Township Rebellion, Upercent, DJ Tennis
- Labels: Afterlife, This Never Happened (Lane 8), Moon Harbour, Sapiens
- Country crossover: Shaboozey, Uncle Kracker, Brett Eldredge
- Hip-hop/rock: MGK, NF, Post Malone, mansionz, Kid Rock
- The sound: "Controlled chaos. Not random — intentional. Structure holding something wild inside."

Rules:
- Never repeat the same song twice
- Know what's CURRENT, not what was good 3 years ago
- Discover NEW music, don't default to old favorites
- BPM ranges: Deep house 118-124, melodic techno 120-128, progressive 122-130
- Always include BPM and key when recommending tracks
- Format: Track — Artist (Label, Year) [BPM, Key]
"""


def render():
    st.markdown("""
    <div style="text-align:center; margin-bottom:16px;">
        <span style="font-size:32px;">🎵</span>
        <h2 style="margin:4px 0;">Simple Balance Music Finder</h2>
        <p style="color:#888; font-size:14px;">DJ assistant. Track discovery. Set building. The sound.</p>
    </div>
    """, unsafe_allow_html=True)

    # Quick action chips
    cols = st.columns(4)
    actions = [
        ("🎧 Deep House", "Find me 5 deep house tracks around 122 BPM that fit the controlled chaos vibe"),
        ("🌙 Late Night", "I need a late night melodic techno set. 3 AM energy. Give me 5 tracks."),
        ("🔥 New Drops", "What's dropped this month in melodic house/techno? Give me the best new releases."),
        ("🎼 Set Builder", "Help me build a 1-hour set. Start deep, build to melodic techno peak, bring it back down."),
    ]

    for i, (label, prompt) in enumerate(actions):
        with cols[i]:
            if st.button(label, key=f"mf_action_{i}", use_container_width=True):
                if "music_finder_chat" not in st.session_state:
                    st.session_state.music_finder_chat = []
                st.session_state.music_finder_chat.append({"role": "user", "content": prompt})
                st.rerun()

    st.divider()

    if "music_finder_chat" not in st.session_state:
        st.session_state.music_finder_chat = []

    render_chat("music_finder_chat", SYSTEM_PROMPT, placeholder="What are we looking for?", input_key="mf_input")
