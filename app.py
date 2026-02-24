"""
Casa Gianelli — Personal Command Center
Peter & Gladys | Family Dashboard
v3.0 — Sidebar Navigation Edition
"""

import streamlit as st
from datetime import datetime
from utils.state import init_state, gl_age

# --- Page Config ---
st.set_page_config(
    page_title="Casa Gianelli",
    page_icon="\U0001f3e0",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialize State ---
init_state()

# --- Page Registry ---
PAGE_GROUPS = {
    "Family HQ": [
        ("Casa", "tab_casa"),
        ("Housing Search", "tab_housing"),
        ("Car Search", "tab_car"),
        ("Grocery List", "tab_grocery"),
        ("Calendar", "tab_calendar"),
        ("Tasks", "tab_tasks"),
    ],
    "Health & Wellness": [
        ("Health Protocol", "tab_health"),
        ("Gladys Beauty", "tab_beauty"),
    ],
    "Entertainment": [
        ("Music Discovery", "tab_music"),
        ("Streaming", "tab_streaming"),
    ],
    "Voice": [
        ("Peter Vomit", "tab_peter_vomit"),
        ("Gladys Bamba", "tab_gladys_bamba"),
    ],
    "GL's World": [
        ("Story Buddy", "tab_story_buddy"),
        ("GL Stories", "tab_gl_stories"),
        ("GL Languages", "tab_gl_languages"),
        ("GL Signs", "tab_gl_signs"),
        ("GL Games", "tab_gl_games"),
        ("GL Milestones", "tab_gl_milestones"),
        ("GL Music", "tab_gl_music"),
    ],
    "AI Tools": [
        ("Music Finder", "tab_music_finder"),
        ("Trend Tracker", "tab_trend_tracker"),
        ("Casa Classic", "tab_casa_classic"),
    ],
    "J.A.W. Music AI": [
        ("J.A.W. Command", "tab_music_jaw"),
        ("Music Discovery", "tab_music_discovery"),
        ("AI Mastering", "tab_music_mastering"),
        ("Stem Separation", "tab_music_stems"),
        ("AI Generation", "tab_music_generation"),
        ("Festival Radar", "tab_music_festivals"),
        ("Set Builder", "tab_music_setbuilder"),
        ("Mix Archive", "tab_music_archive"),
        ("Producer Tools", "tab_music_producer"),
        ("Music Dashboard", "tab_music_dashboard"),
    ],
}

# --- CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Lato:wght@300;400;600;700&display=swap');

    /* Sidebar - Dark warm theme */
    [data-testid="stSidebar"] {
        background-color: #1A0F0F;
        border-right: 1px solid #2D1A1A;
    }
    [data-testid="stSidebar"] * {
        color: #e8ddd0 !important;
    }
    [data-testid="stSidebar"] .stButton button {
        background-color: #1A0F0F !important;
        color: #D4A017 !important;
        border: 1px solid #3D2A2A !important;
        font-weight: 600 !important;
        text-align: left !important;
        padding: 8px 12px !important;
        font-size: 13px !important;
    }
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #C41E3A !important;
        color: #ffffff !important;
        border-color: #C41E3A !important;
    }

    /* Main content - Dark theme */
    .stApp {
        background-color: #0D0D1A;
        color: #FFFEF7;
    }
    .stApp [data-testid="stAppViewContainer"] {
        background-color: #0D0D1A;
    }
    .stApp [data-testid="stHeader"] { background-color: transparent; }
    .stApp footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    .stApp p, .stApp span, .stApp label, .stApp li { color: #FFFEF7; }
    .stApp .stMarkdown { color: #FFFEF7; }

    /* Header */
    .main-header {
        background: linear-gradient(135deg, #1A0F0F 0%, #3D1A1A 50%, #C41E3A 100%);
        padding: 28px 32px;
        border-radius: 12px;
        margin-bottom: 24px;
        border: 1px solid #C41E3A;
    }
    .main-header h1 {
        font-family: 'Playfair Display', serif;
        color: #ffffff;
        font-size: 28px;
        margin: 0;
        font-weight: 700;
    }
    .main-header p {
        color: #D4A017;
        font-size: 14px;
        margin: 4px 0 0 0;
        font-weight: 500;
        font-style: italic;
    }

    /* Feature cards - glass morphism */
    .feature-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #C41E3A;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        border-color: #D4A017;
        background: rgba(212,160,23,0.08);
    }
    .feature-card h4 {
        color: #FFE082;
        margin: 0 0 8px 0;
        font-size: 15px;
    }
    .feature-card p {
        color: #8A7A5A;
        font-size: 13px;
        margin: 0;
    }

    /* General styling */
    h1, h2, h3 { color: #D4A017 !important; }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #C41E3A, #8B0000);
        border: none;
    }
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #D4A017, #B8860B);
    }
    .stButton > button[kind="secondary"] {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #FFFEF7 !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background: rgba(212,160,23,0.15) !important;
        border-color: #D4A017 !important;
    }
    a { color: #D4A017 !important; }

    /* Chat messages - dark */
    .stChatMessage {
        background-color: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 10px !important;
    }
    .stChatInput input {
        background-color: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #FFFEF7 !important;
    }
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background-color: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #FFFEF7 !important;
    }
    .stDivider { border-color: rgba(255,255,255,0.08) !important; }
    .stExpander { border-color: rgba(255,255,255,0.08) !important; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
if "selected_page" not in st.session_state:
    st.session_state.selected_page = None

with st.sidebar:
    # Logo / branding
    st.markdown("""
    <div style="text-align: center; padding: 8px 0 12px 0;">
        <div style="background: linear-gradient(135deg, #C41E3A, #D4A017); width: 44px; height: 44px; border-radius: 10px; display: inline-flex; align-items: center; justify-content: center; font-size: 22px; color: white;">\U0001f3e0</div>
        <p style="color: #D4A017 !important; font-size: 14px; font-weight: 700; margin: 6px 0 0 0; letter-spacing: 0.5px; font-family: 'Playfair Display', serif;">Casa Gianelli</p>
        <p style="color: #8a7a6a !important; font-size: 11px; margin: 2px 0 0 0; font-style: italic;">La Familia</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # GL age display
    age = gl_age()
    st.markdown(f"""
    <div style="text-align: center; padding: 4px 0 8px 0;">
        <p style="color: #8a7a6a !important; font-size: 11px; margin: 0;">Gian Lucca: <span style="color: #D4A017 !important;">{age['months']:.1f} months</span></p>
        <p style="color: #8a7a6a !important; font-size: 10px; margin: 2px 0 0 0;">Day {age['day_1000']} of 1,000</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Navigation buttons grouped by section
    for group_name, pages in PAGE_GROUPS.items():
        if group_name == "GL's World":
            st.markdown(f"""
            <div style="margin: 16px 0 8px 0; padding-top: 10px; border-top: 1px solid rgba(212,160,23,0.3);">
                <p style="color: #D4A017 !important; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin: 0;">\U0001f476 GL's World</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <p style="color: #D4A017 !important; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin: 16px 0 8px 0;">{group_name}</p>
            """, unsafe_allow_html=True)

        for page_name, module_name in pages:
            is_selected = st.session_state.selected_page == module_name
            if st.button(
                page_name,
                key=f"nav_{module_name}",
                use_container_width=True,
                type="primary" if is_selected else "secondary",
            ):
                st.session_state.selected_page = module_name
                st.rerun()

    st.markdown("---")

    # Live counts
    tasks = st.session_state.get("tasks", [])
    done_tasks = sum(1 for t in tasks if t.get("done"))
    signs = len(st.session_state.get("gl_signs_learned", []))
    milestones = len(st.session_state.get("gl_milestones_done", []))

    st.markdown(f"""
    <div style="font-size: 11px; color: #8a7a6a !important;">
        <p style="margin: 4px 0;">Tasks: {done_tasks}/{len(tasks)} done</p>
        <p style="margin: 4px 0;">GL Signs: {signs}/18</p>
        <p style="margin: 4px 0;">GL Milestones: {milestones}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: #5a4a3a !important; font-size: 10px; margin: 0;">Casa Gianelli v5.0</p>
        <p style="color: #5a4a3a !important; font-size: 10px; margin: 2px 0 0 0;">Built by Sinton.ia</p>
    </div>
    """, unsafe_allow_html=True)


# --- Page Routing ---
selected = st.session_state.selected_page

# Landing page (when nothing selected)
if selected is None:
    st.markdown("""
    <div class="main-header">
        <h1>Casa Gianelli</h1>
        <p>La Familia. Peter & Gladys & Gian Lucca.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="max-width: 900px; margin: 0 auto;">

<h2 style="color: #FFE082 !important; text-align: center; margin-bottom: 8px;">Your <span style="color: #C41E3A;">FAMILY</span> command center.</h2>
<p style="color: #8A7A5A; text-align: center; font-size: 15px; margin-bottom: 32px;">Everything in one place. Housing, health, groceries, car, GL's development, entertainment, AI tools, and more.</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">
    <div class="feature-card" style="border-left-color: #C41E3A;">
        <h4>Family HQ</h4>
        <p>Shopping, housing search, car search, groceries, calendar, and tasks. All the logistics.</p>
    </div>
    <div class="feature-card" style="border-left-color: #006847;">
        <h4>Health & Wellness</h4>
        <p>Peter's protocol, Gladys's protocol. Injection tracker, weekly check-ins, weight chart.</p>
    </div>
    <div class="feature-card" style="border-left-color: #D4A017;">
        <h4>Entertainment</h4>
        <p>Music discovery by mood. Streaming recommendations. Peter and Gladys watchlist.</p>
    </div>
    <div class="feature-card" style="border-left-color: #8B4513;">
        <h4>GL's World</h4>
        <p>Story Buddy, languages, sign language, brain games, milestones, music lab. GL's First 1,000 Days.</p>
    </div>
</div>

<div style="background: linear-gradient(135deg, #1A0F0F, #C41E3A); border-radius: 10px; padding: 20px; text-align: center; margin-bottom: 16px;">
    <p style="color: #D4A017; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Get Started</p>
    <p style="color: #ffffff; font-size: 14px;">Select a page from the sidebar.</p>
</div>

<p style="color: #555; text-align: center; font-size: 12px;">32 pages. Everything works. One family.</p>
<p style="color: #444; text-align: center; font-size: 11px;">Built by Sinton.ia</p>

</div>
""", unsafe_allow_html=True)

    st.stop()

# --- Header for selected page ---
st.markdown("""
<div class="main-header">
    <h1>Casa Gianelli</h1>
    <p>La Familia. Peter & Gladys & Gian Lucca.</p>
</div>
""", unsafe_allow_html=True)

# --- Render selected page ---
from tabs import tab_casa, tab_housing, tab_car, tab_health, tab_beauty
from tabs import tab_grocery, tab_music, tab_streaming, tab_calendar
from tabs import tab_peter_vomit, tab_gladys_bamba, tab_tasks
from tabs import tab_story_buddy, tab_gl_stories
from tabs import tab_gl_languages, tab_gl_signs, tab_gl_games
from tabs import tab_gl_milestones, tab_gl_music
from tabs import tab_music_finder, tab_trend_tracker, tab_casa_classic
from tabs import tab_music_jaw, tab_music_discovery, tab_music_mastering
from tabs import tab_music_stems, tab_music_generation, tab_music_festivals
from tabs import tab_music_setbuilder, tab_music_archive, tab_music_producer
from tabs import tab_music_dashboard

PAGE_MODULES = {
    "tab_casa": tab_casa,
    "tab_housing": tab_housing,
    "tab_car": tab_car,
    "tab_health": tab_health,
    "tab_beauty": tab_beauty,
    "tab_grocery": tab_grocery,
    "tab_music": tab_music,
    "tab_streaming": tab_streaming,
    "tab_calendar": tab_calendar,
    "tab_peter_vomit": tab_peter_vomit,
    "tab_gladys_bamba": tab_gladys_bamba,
    "tab_tasks": tab_tasks,
    "tab_story_buddy": tab_story_buddy,
    "tab_gl_stories": tab_gl_stories,
    "tab_gl_languages": tab_gl_languages,
    "tab_gl_signs": tab_gl_signs,
    "tab_gl_games": tab_gl_games,
    "tab_gl_milestones": tab_gl_milestones,
    "tab_gl_music": tab_gl_music,
    "tab_music_finder": tab_music_finder,
    "tab_trend_tracker": tab_trend_tracker,
    "tab_casa_classic": tab_casa_classic,
    "tab_music_jaw": tab_music_jaw,
    "tab_music_discovery": tab_music_discovery,
    "tab_music_mastering": tab_music_mastering,
    "tab_music_stems": tab_music_stems,
    "tab_music_generation": tab_music_generation,
    "tab_music_festivals": tab_music_festivals,
    "tab_music_setbuilder": tab_music_setbuilder,
    "tab_music_archive": tab_music_archive,
    "tab_music_producer": tab_music_producer,
    "tab_music_dashboard": tab_music_dashboard,
}

module = PAGE_MODULES.get(selected)
if module:
    module.render()
