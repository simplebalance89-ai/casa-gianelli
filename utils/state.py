"""Central session_state initialization for Casa Gianelli."""
import streamlit as st
from datetime import datetime


def init_state():
    """Initialize all session_state keys with defaults. Called once at app start."""
    defaults = {
        # Grocery
        "grocery_items": {
            "Electrolytes / Health": [
                "LMNT packets (or similar no-sugar electrolyte)",
                "NoSalt or NuSalt (potassium salt substitute)",
                "Sea salt or Himalayan pink salt",
                "Lemons",
                "Coconut water (backup)",
            ],
            "Better Broth / Stock": [
                "Bone broth (Kettle & Fire — low sodium)",
                "Low-sodium chicken stock",
                "Beef bone broth",
            ],
            "Protein (200g+ daily goal)": [
                "Chicken breast",
                "Ground turkey",
                "Eggs",
                "Greek yogurt (plain, full fat)",
                "Cottage cheese",
            ],
            "Staples": [],
            "Costco": [],
            "Baby": [],
        },
        "grocery_checked": {},

        # Tasks
        "tasks": [
            {"text": "Send Andrew email + invoice", "assignee": "Peter", "done": False},
            {"text": "Andrew meeting prep", "assignee": "Peter", "done": False},
            {"text": "Fix MCP permissions", "assignee": "Peter", "done": False},
            {"text": "Get on VM for M4 Knick SQL", "assignee": "Peter", "done": False},
            {"text": "Connect Pwgcerp to Microsoft MCP", "assignee": "Peter", "done": False},
            {"text": "Review health protocol", "assignee": "Gladys", "done": False},
            {"text": "Gladys Beauty scheduling", "assignee": "Gladys", "done": False},
        ],

        # Health
        "injection_log": [],
        "checkin_log": [],

        # Vomit / Bamba
        "peter_drops": [],
        "gladys_drops": [],

        # Housing picks
        "housing_picks": [],

        # Car picks
        "car_picks": [],

        # Watchlist
        "watchlist": [],

        # Calendar events
        "events": [
            {"title": "Weekly Check-In (Health)", "date": "Sunday", "who": "Both", "type": "Reminder"},
        ],

        # GL tracking
        "gl_signs_learned": [],
        "gl_milestones_done": [],
        "gl_vocab_practiced": [],
        "gl_games_done": [],
        "gl_music_reactions": [],

        # Chat histories
        "sb_messages": [],
        "sb_started": False,
        "gl_sb_messages": [],
        "gl_sb_started": False,
        "gl_lang_messages": [],
        "gl_signs_messages": [],
        "gl_games_messages": [],
        "gl_miles_messages": [],
        "gl_music_messages": [],
    }
    for key, default in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default


def gl_age():
    """Return GL's age info as a dict."""
    born = datetime(2025, 7, 27)
    today = datetime.now()
    days = (today - born).days
    months = days / 30.44
    weeks = days // 7
    day_1000 = days + 270
    return {"days": days, "months": months, "weeks": weeks, "day_1000": day_1000}
