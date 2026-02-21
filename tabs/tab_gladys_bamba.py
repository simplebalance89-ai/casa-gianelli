import streamlit as st
from datetime import datetime


def render():
    st.header("Gladys Bamba")
    st.caption("Todo lo que necesitas soltar. Sin filtro.")

    if "gladys_drops" not in st.session_state:
        st.session_state.gladys_drops = []

    # Input section
    with st.form("gladys_bamba_form", clear_on_submit=True):
        content = st.text_area(
            "Dime todo:",
            height=150,
            placeholder="Escribe lo que sea. Grocery list, appointment, idea, whatever.",
        )
        category = st.selectbox(
            "Category",
            ["Groceries", "Baby/GL", "Beauty Business", "Appointment",
             "Shopping", "Home", "Personal", "Other"],
        )
        submitted = st.form_submit_button("Send It")
        if submitted and content.strip():
            st.session_state.gladys_drops.insert(0, {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "category": category,
                "content": content.strip(),
            })
            st.rerun()

    st.divider()

    # Recent Submissions
    st.subheader("Recent Submissions")
    drops = st.session_state.gladys_drops[:20]

    if drops:
        cat_colors = {
            "Groceries": "green",
            "Baby/GL": "red",
            "Beauty Business": "violet",
            "Appointment": "blue",
            "Shopping": "orange",
            "Home": "gray",
            "Personal": "rainbow",
            "Other": "gray",
        }
        for i, drop in enumerate(drops):
            color = cat_colors.get(drop["category"], "gray")
            st.markdown(f"**{drop['timestamp']}** &nbsp; :{color}[{drop['category']}]")
            st.markdown(drop["content"])
            if i < len(drops) - 1:
                st.divider()
    else:
        st.caption("Nothing here yet. Send something above.")

    # Stats
    if st.session_state.gladys_drops:
        st.divider()
        total = len(st.session_state.gladys_drops)
        st.caption(f"Total submissions: {total}")
