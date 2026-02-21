"""Streaming tab - Show & movie recommendations, watchlist, services."""
import streamlit as st
from datetime import datetime


def render():
    st.header("Shows & Movies to Stream")

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Sinton.ia Recommends")

        st.markdown("#### Shows")
        shows = [
            ("Severance", "Apple TV+", "Mind-bending sci-fi. Work/life split taken literally. Right up your alley."),
            ("The Bear", "Hulu", "Kitchen chaos, family pressure, anxiety as fuel. You'll feel this one."),
            ("Beef", "Netflix", "Road rage spirals into life destruction. Dark comedy, empath test."),
            ("Shogun", "Hulu/FX", "Strategy, honor, power. Slow burn but massive payoff."),
            ("Reacher", "Prime", "No-nonsense problem solver. Turn off your brain and enjoy."),
            ("Fallout", "Prime", "Post-apocalyptic dark comedy. Surprisingly deep."),
            ("3 Body Problem", "Netflix", "Science meets conspiracy. Heavy but rewarding."),
            ("Slow Horses", "Apple TV+", "British spy rejects who are actually the best. Dry humor."),
        ]
        for title, platform, why in shows:
            with st.expander(f"{title} \u2014 {platform}"):
                st.markdown(why)

        st.markdown("#### Movies")
        movies = [
            ("Past Lives", "Prime", "What-ifs and parallel lives. Quiet but hits hard."),
            ("The Holdovers", "Peacock", "Lonely teacher, lonely kid. Paul Giamatti is perfect."),
            ("Oppenheimer", "Peacock", "If you haven't seen it yet. The weight of creation."),
            ("Ferrari", "Hulu", "Racing, passion, Italian heritage. Family and ambition."),
            ("Hit Man", "Netflix", "Dark comedy. Playing a character so well you become it."),
            ("Civil War", "Max", "Journalists in a broken America. Intense and relevant."),
        ]
        for title, platform, why in movies:
            with st.expander(f"{title} \u2014 {platform}"):
                st.markdown(why)

    with col_right:
        st.subheader("Peter & Gladys Watchlist")

        with st.form("add_watchlist", clear_on_submit=True):
            w_title = st.text_input("Title")
            w_type = st.selectbox("Type", ["Show", "Movie", "Documentary"])
            w_platform = st.selectbox("Platform", [
                "Netflix", "Hulu", "Prime", "Apple TV+", "Max",
                "Peacock", "Disney+", "Paramount+", "Other",
            ])
            w_notes = st.text_area("Notes / Who recommended", height=68)
            submitted = st.form_submit_button("Add to Watchlist")
            if submitted and w_title.strip():
                st.session_state.watchlist.append({
                    "title": w_title.strip(),
                    "platform": w_platform,
                    "type": w_type,
                    "notes": w_notes,
                    "added": datetime.now().strftime("%Y-%m-%d"),
                })
                st.rerun()

        if st.session_state.watchlist:
            for i, item in enumerate(st.session_state.watchlist):
                c1, c2 = st.columns([4, 1])
                c1.markdown(f"**{item['title']}** ({item['platform']}) - {item['type']}")
                if c2.button("X", key=f"rm_watch_{i}"):
                    st.session_state.watchlist.pop(i)
                    st.rerun()
        else:
            st.caption("Watchlist is empty. Add something above.")

        st.divider()

        st.subheader("Currently Watching")
        if "currently_watching" not in st.session_state:
            st.session_state.currently_watching = ""
        with st.form("currently_watching_form"):
            current = st.text_input("Show/Movie:", value=st.session_state.currently_watching)
            watch_status = st.selectbox("Status:", ["Watching", "Paused", "Finished", "Dropped"])
            if st.form_submit_button("Update"):
                st.session_state.currently_watching = current.strip()
                st.rerun()

        if st.session_state.currently_watching:
            st.info(f"Now watching: **{st.session_state.currently_watching}**")

        st.divider()

        st.subheader("Streaming Services")
        services = {
            "Netflix": "Active",
            "Hulu": "Active",
            "Amazon Prime": "Active",
            "Apple TV+": "Check",
            "Max (HBO)": "Check",
            "Peacock": "Check",
            "Disney+": "Check",
            "Paramount+": "Check",
            "Spotify": "Active",
            "Tidal": "Active",
        }
        for svc, status in services.items():
            icon = "+" if status == "Active" else "?"
            st.markdown(f"**{icon} {svc}** \u2014 {status}")
