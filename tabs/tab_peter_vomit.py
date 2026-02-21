import streamlit as st
from datetime import datetime


def render():
    st.header("Peter Vomit")
    st.caption("Brain dump. No filter. Drop it and move on.")

    if "peter_drops" not in st.session_state:
        st.session_state.peter_drops = []

    # Input section
    with st.form("peter_vomit_form", clear_on_submit=True):
        content = st.text_area(
            "What's in your head?",
            height=150,
            placeholder="Just start typing. No structure needed.",
        )
        tag = st.selectbox(
            "Tag it",
            ["Work", "Personal", "Idea", "Family", "Music", "Health", "Money", "Random"],
        )
        submitted = st.form_submit_button("Drop the Bomba")
        if submitted and content.strip():
            st.session_state.peter_drops.insert(0, {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "tag": tag,
                "content": content.strip(),
            })
            st.rerun()

    st.divider()

    # Recent Drops
    st.subheader("Recent Drops")
    drops = st.session_state.peter_drops[:20]

    if drops:
        tag_colors = {
            "Work": "blue",
            "Personal": "green",
            "Idea": "orange",
            "Family": "red",
            "Music": "violet",
            "Health": "rainbow",
            "Money": "green",
            "Random": "gray",
        }
        for i, drop in enumerate(drops):
            color = tag_colors.get(drop["tag"], "gray")
            st.markdown(f"**{drop['timestamp']}** &nbsp; :{color}[{drop['tag']}]")
            st.markdown(drop["content"])
            if i < len(drops) - 1:
                st.divider()
    else:
        st.caption("Nothing here yet. Drop something above.")

    # Stats
    if st.session_state.peter_drops:
        st.divider()
        total = len(st.session_state.peter_drops)
        st.caption(f"Total drops: {total}")
