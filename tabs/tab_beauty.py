import streamlit as st
from datetime import datetime, date


def render():
    st.header("Gladys Beauty")

    # Initialize session state
    if "beauty_clients" not in st.session_state:
        st.session_state.beauty_clients = []
    if "beauty_appointments" not in st.session_state:
        st.session_state.beauty_appointments = []

    # --- Price List ---
    st.subheader("Lash Services Price List")

    prices = [
        ("Classic Full Set", "$150"),
        ("Hybrid Full Set", "$180"),
        ("Volume Full Set", "$200"),
        ("Classic Fill (2-3 weeks)", "$85"),
        ("Hybrid Fill (2-3 weeks)", "$100"),
        ("Volume Fill (2-3 weeks)", "$120"),
        ("Lash Removal", "$40"),
    ]

    col1, col2 = st.columns(2)
    for i, (service, price) in enumerate(prices):
        if i < 4:
            with col1:
                st.write(f"**{service}** .... {price}")
        else:
            with col2:
                st.write(f"**{service}** .... {price}")

    # --- Client List ---
    st.divider()
    st.subheader("Clients")

    with st.form("add_client", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            client_name = st.text_input("Client Name")
        with col2:
            client_phone = st.text_input("Phone")
        with col3:
            client_last_visit = st.date_input("Last Visit", value=date.today(), key="client_lv")

        if st.form_submit_button("Add Client"):
            if client_name:
                st.session_state.beauty_clients.append({
                    "name": client_name,
                    "phone": client_phone,
                    "last_visit": client_last_visit.strftime("%Y-%m-%d"),
                    "added": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                st.success(f"Added: {client_name}")
                st.rerun()

    if st.session_state.beauty_clients:
        st.markdown("**Client List:**")
        for i, client in enumerate(st.session_state.beauty_clients):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.write(client["name"])
            with col2:
                st.write(client["phone"])
            with col3:
                st.write(f"Last: {client['last_visit']}")
            with col4:
                if st.button("X", key=f"remove_client_{i}"):
                    st.session_state.beauty_clients.pop(i)
                    st.rerun()
    else:
        st.info("No clients yet.")

    # --- Appointment Log ---
    st.divider()
    st.subheader("Appointment Log")

    service_options = [
        "Classic Full Set",
        "Hybrid Full Set",
        "Volume Full Set",
        "Classic Fill",
        "Hybrid Fill",
        "Volume Fill",
        "Lash Removal",
    ]

    # Build client name list for dropdown
    client_names = [c["name"] for c in st.session_state.beauty_clients]
    if not client_names:
        client_names = ["(Add clients first)"]

    with st.form("add_appointment", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            appt_client = st.selectbox("Client", client_names)
        with col2:
            appt_date = st.date_input("Date", value=date.today(), key="appt_date")
        with col3:
            appt_service = st.selectbox("Service", service_options)

        appt_notes = st.text_input("Notes", key="appt_notes")

        if st.form_submit_button("Log Appointment"):
            if appt_client and appt_client != "(Add clients first)":
                st.session_state.beauty_appointments.append({
                    "client": appt_client,
                    "date": appt_date.strftime("%Y-%m-%d"),
                    "service": appt_service,
                    "notes": appt_notes,
                    "logged": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                # Update last visit for this client
                for c in st.session_state.beauty_clients:
                    if c["name"] == appt_client:
                        c["last_visit"] = appt_date.strftime("%Y-%m-%d")
                        break
                st.success(f"Logged: {appt_service} for {appt_client}")
                st.rerun()

    if st.session_state.beauty_appointments:
        st.markdown("**Recent Appointments:**")
        for appt in reversed(st.session_state.beauty_appointments[-15:]):
            note_text = f" - {appt['notes']}" if appt['notes'] else ""
            st.write(f"- {appt['date']} | {appt['client']} | {appt['service']}{note_text}")
    else:
        st.info("No appointments logged yet.")

    # --- Quick Stats ---
    st.divider()
    st.subheader("Quick Stats")
    total_clients = len(st.session_state.beauty_clients)
    total_appts = len(st.session_state.beauty_appointments)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Clients", total_clients)
    with col2:
        st.metric("Total Appointments", total_appts)
