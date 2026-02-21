"""Health Protocol tab - 6 Week Program with injection tracker and weekly check-ins."""
import streamlit as st
from datetime import datetime, date


def render():
    st.header("Health Protocol \u2014 6 Week Program")

    # --- Protocol Week Tracker ---
    protocol_start = date(2026, 1, 25)
    today = date.today()
    days_in = (today - protocol_start).days
    week_num = min((days_in // 7) + 1, 6)

    if days_in < 0:
        st.info("Protocol hasn't started yet.")
    elif week_num <= 6:
        st.metric("Protocol Progress", f"Week {week_num} of 6", f"Day {days_in + 1}")
        st.progress(min(days_in / 42, 1.0))
    else:
        st.success("6-week protocol complete!")

    st.divider()

    # --- Person toggle ---
    person = st.radio("View Protocol For:", ["Peter", "Gladys"], horizontal=True)

    if person == "Peter":
        st.subheader("Peter's Goals")
        st.markdown("""
        - Lose 20-30 lbs in 6 weeks
        - Reduce inflammation and joint pain
        - Manage anxiety/OCD naturally
        - Improve sleep quality
        - Brain repair from past substance use
        - Liver protection during protocol
        """)

        st.subheader("Foundation Phase (Weeks 1-6)")
        peter_foundation = {
            "N-Acetyl Selank": {"dose": "250mcg", "timing": "Daily AM", "purpose": "Anxiety, OCD, cortisol reduction"},
            "BPC-157": {"dose": "500mcg", "timing": "Daily AM", "purpose": "Inflammation, joint pain, gut healing"},
            "CJC-1295/Ipamorelin": {"dose": "Per vial", "timing": "PM before bed", "purpose": "Sleep, fat loss, recovery"},
            "Testosterone Propionate": {"dose": "50mg", "timing": "EOD (Mon/Wed/Fri/Sun)", "purpose": "Stable energy, muscle preservation"},
        }
        for compound, info in peter_foundation.items():
            with st.expander(f"{compound} \u2014 {info['dose']}"):
                st.markdown(f"**Timing:** {info['timing']}")
                st.markdown(f"**Purpose:** {info['purpose']}")

        st.subheader("Test Prop Schedule")
        st.markdown("**Started:** Sunday Jan 25, 2026 | **Dose:** 0.5ml (50mg) IM")
        st.markdown("**Site rotation:** R shoulder \u2192 L shoulder \u2192 R thigh \u2192 L thigh \u2192 repeat")

    else:
        st.subheader("Gladys's Goals")
        st.markdown("""
        - Lose 10-16 lbs in 6 weeks
        - Improve sleep quality (critical with Gian Lucca)
        - Heal postpartum tissue damage
        - Regulate period/hormones
        - Skin tightening and collagen repair
        - Address postpartum hair thinning
        """)

        st.subheader("Foundation Phase (Weeks 1-6)")
        gladys_foundation = {
            "BPC-157": {"dose": "250mcg", "timing": "Daily AM", "purpose": "Postpartum healing, skin tightening"},
            "GHK-Cu": {"dose": "2mg", "timing": "Daily AM", "purpose": "Skin tightening, collagen, hair"},
            "AOD-9604": {"dose": "300mcg", "timing": "Daily AM fasted", "purpose": "Stubborn belly fat"},
            "CJC-1295/Ipamorelin": {"dose": "Per vial", "timing": "PM before bed", "purpose": "CRITICAL for sleep with baby"},
        }
        for compound, info in gladys_foundation.items():
            with st.expander(f"{compound} \u2014 {info['dose']}"):
                st.markdown(f"**Timing:** {info['timing']}")
                st.markdown(f"**Purpose:** {info['purpose']}")

    # --- Injection Tracker ---
    st.divider()
    st.subheader("Injection Tracker")

    rotation = ["R Shoulder", "L Shoulder", "R Thigh", "L Thigh"]
    if st.session_state.injection_log:
        last_site = st.session_state.injection_log[-1]["site"]
        if last_site in rotation:
            next_idx = (rotation.index(last_site) + 1) % len(rotation)
        else:
            next_idx = 0
    else:
        next_idx = 0

    next_site = rotation[next_idx]
    st.info(f"Next site: **{next_site}**")

    with st.form("injection_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            inj_date = st.date_input("Date", value=date.today(), key="inj_date")
            inj_site = st.selectbox("Injection Site", rotation, index=next_idx)
        with col2:
            inj_compound = st.selectbox("Compound", [
                "Testosterone Propionate",
                "N-Acetyl Selank",
                "BPC-157",
                "CJC-1295/Ipamorelin",
                "GHK-Cu",
                "AOD-9604",
                "Other",
            ])
            inj_notes = st.text_input("Notes")

        if st.form_submit_button("Log Injection"):
            st.session_state.injection_log.append({
                "date": inj_date.strftime("%Y-%m-%d"),
                "site": inj_site,
                "compound": inj_compound,
                "notes": inj_notes,
            })
            st.success(f"Logged: {inj_compound} in {inj_site}")
            st.rerun()

    if st.session_state.injection_log:
        st.markdown("**Recent Injections:**")
        recent = st.session_state.injection_log[-10:][::-1]
        for entry in recent:
            note_text = f" - {entry['notes']}" if entry['notes'] else ""
            st.write(f"- {entry['date']} | {entry['compound']} | {entry['site']}{note_text}")

    # --- Weekly Check-In ---
    st.divider()
    st.subheader("Weekly Check-In (Sundays)")

    with st.form("checkin_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            ci_date = st.date_input("Date", value=date.today(), key="ci_date")
            ci_weight = st.number_input("Weight (lbs)", min_value=100.0, max_value=400.0, value=185.0, step=0.5)
        with col2:
            ci_energy = st.slider("Energy (1-10)", 1, 10, 5)
            ci_sleep = st.slider("Sleep Quality (1-10)", 1, 10, 5)
        with col3:
            ci_mood = st.slider("Mood (1-10)", 1, 10, 5)
            ci_libido = st.slider("Libido (1-10)", 1, 10, 5)

        ci_notes = st.text_area("Notes / Side Effects", height=68, key="ci_notes")

        if st.form_submit_button("Save Check-In"):
            st.session_state.checkin_log.append({
                "date": ci_date.strftime("%Y-%m-%d"),
                "weight": ci_weight,
                "energy": ci_energy,
                "sleep": ci_sleep,
                "mood": ci_mood,
                "libido": ci_libido,
                "notes": ci_notes,
            })
            st.success("Check-in saved!")
            st.rerun()

    if st.session_state.checkin_log:
        st.markdown("**Check-In History:**")
        for entry in reversed(st.session_state.checkin_log[-10:]):
            st.write(
                f"- {entry['date']} | {entry['weight']} lbs | "
                f"Energy: {entry['energy']} | Sleep: {entry['sleep']} | "
                f"Mood: {entry['mood']} | Libido: {entry['libido']}"
            )
            if entry["notes"]:
                st.caption(f"  Notes: {entry['notes']}")

        # Weight chart
        if len(st.session_state.checkin_log) >= 2:
            try:
                import plotly.graph_objects as go

                dates = [e["date"] for e in st.session_state.checkin_log]
                weights = [e["weight"] for e in st.session_state.checkin_log]

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=dates, y=weights,
                    mode="lines+markers",
                    name="Weight",
                    line=dict(color="#FF6B6B", width=2),
                    marker=dict(size=8),
                ))
                fig.update_layout(
                    title="Weight Over Time",
                    xaxis_title="Date",
                    yaxis_title="Weight (lbs)",
                    height=300,
                    margin=dict(l=20, r=20, t=40, b=20),
                )
                st.plotly_chart(fig, use_container_width=True)
            except ImportError:
                st.warning("Install plotly for weight chart: pip install plotly")
