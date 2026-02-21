import streamlit as st
from datetime import datetime, timedelta, time as dt_time


def render():
    st.header("Calendar")

    if "events" not in st.session_state:
        st.session_state.events = []

    # Add Event form
    st.subheader("Add Event")
    with st.form("add_event", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Event Title")
            event_date = st.date_input("Date", value=datetime.now().date())
            event_time = st.time_input("Time", value=dt_time(9, 0))
        with col2:
            who = st.selectbox("Who", ["Peter", "Gladys", "Both", "Family", "GL"])
            event_type = st.selectbox("Type", [
                "Meeting", "Appointment", "Deadline", "Personal",
                "Health", "Family", "Work", "Other",
            ])
        submitted = st.form_submit_button("Add Event")
        if submitted and title.strip():
            st.session_state.events.append({
                "title": title.strip(),
                "date": event_date.isoformat(),
                "time": event_time.strftime("%H:%M"),
                "who": who,
                "type": event_type,
            })
            st.rerun()

    st.divider()

    # This Week
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    st.subheader(f"This Week ({start_of_week.strftime('%b %d')} - {end_of_week.strftime('%b %d')})")
    week_events = [
        e for e in st.session_state.events
        if start_of_week <= datetime.fromisoformat(e["date"]).date() <= end_of_week
    ]
    week_events.sort(key=lambda e: (e["date"], e["time"]))

    if week_events:
        for e in week_events:
            dt = datetime.fromisoformat(e["date"])
            st.markdown(
                f"- **{dt.strftime('%a %b %d')}** {e['time']} | "
                f"{e['title']} ({e['who']}) [{e['type']}]"
            )
    else:
        st.caption("No events this week.")

    st.divider()

    # All Events
    st.subheader("All Events")
    sorted_events = sorted(
        st.session_state.events,
        key=lambda e: (e["date"], e["time"]),
    )

    if sorted_events:
        for i, e in enumerate(sorted_events):
            original_idx = st.session_state.events.index(e)
            dt = datetime.fromisoformat(e["date"])
            c1, c2 = st.columns([5, 1])
            c1.markdown(
                f"**{dt.strftime('%b %d, %Y')}** {e['time']} | "
                f"{e['title']} ({e['who']}) [{e['type']}]"
            )
            if c2.button("Remove", key=f"rm_evt_{i}"):
                st.session_state.events.pop(original_idx)
                st.rerun()
    else:
        st.caption("No events yet. Add one above.")

    st.divider()

    # Key Dates (reference)
    st.subheader("Key Dates (Reference)")
    key_dates = [
        ("Andrew meeting", "Recurring weekly check-in"),
        ("Housing decision", "Palm Springs move timeline"),
        ("Palm Springs move", "Target relocation date"),
        ("C365 contract", "Conveyance365 contract milestones"),
        ("Health check-ins", "Regular health appointments"),
        ("GL monthly milestones", "Gladys Lucia developmental milestones"),
    ]
    for label, desc in key_dates:
        st.markdown(f"- **{label}**: {desc}")

    st.divider()

    # Outlook Integration Status
    st.subheader("Outlook Integration Status")
    st.info(
        "Outlook calendar sync is read-only reference. "
        "Events added here are local to this app session."
    )
    accounts = [
        ("peter@conveyance365.com", "Work", "Connected"),
        ("peter.gianelli@gmail.com", "Personal", "Connected"),
    ]
    for email, label, status in accounts:
        st.markdown(f"- **{label}** ({email}): {status}")
