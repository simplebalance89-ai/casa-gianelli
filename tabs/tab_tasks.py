import streamlit as st
from datetime import datetime


def render():
    st.header("Tasks")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Add Task form
    with st.form("add_task_form", clear_on_submit=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            task_text = st.text_input("Task", placeholder="What needs to get done?")
        with col2:
            assignee = st.selectbox("Assignee", ["Peter", "Gladys", "Both"])
        submitted = st.form_submit_button("Add Task")
        if submitted and task_text.strip():
            st.session_state.tasks.append({
                "text": task_text.strip(),
                "assignee": assignee,
                "done": False,
            })
            st.rerun()

    st.divider()

    # Filter tasks per person
    peter_tasks = [
        (i, t) for i, t in enumerate(st.session_state.tasks)
        if t["assignee"] in ("Peter", "Both")
    ]
    gladys_tasks = [
        (i, t) for i, t in enumerate(st.session_state.tasks)
        if t["assignee"] in ("Gladys", "Both")
    ]

    col_peter, col_gladys = st.columns(2)

    with col_peter:
        st.subheader("Peter's Tasks")
        peter_done = sum(1 for _, t in peter_tasks if t["done"])
        peter_total = len(peter_tasks)
        if peter_total:
            st.progress(peter_done / peter_total)
            st.caption(f"{peter_done} of {peter_total} done")
        else:
            st.caption("No tasks.")

        for idx, task in peter_tasks:
            checked = st.checkbox(
                task["text"],
                value=task["done"],
                key=f"peter_task_{idx}",
            )
            if checked != task["done"]:
                st.session_state.tasks[idx]["done"] = checked
                st.rerun()

    with col_gladys:
        st.subheader("Gladys's Tasks")
        gladys_done = sum(1 for _, t in gladys_tasks if t["done"])
        gladys_total = len(gladys_tasks)
        if gladys_total:
            st.progress(gladys_done / gladys_total)
            st.caption(f"{gladys_done} of {gladys_total} done")
        else:
            st.caption("No tasks.")

        for idx, task in gladys_tasks:
            checked = st.checkbox(
                task["text"],
                value=task["done"],
                key=f"gladys_task_{idx}",
            )
            if checked != task["done"]:
                st.session_state.tasks[idx]["done"] = checked
                st.rerun()

    st.divider()

    # Delete Completed
    completed_count = sum(1 for t in st.session_state.tasks if t["done"])
    total_count = len(st.session_state.tasks)

    col_a, col_b = st.columns([2, 1])
    col_a.caption(f"Total: {total_count} tasks | {completed_count} completed")
    if completed_count > 0:
        if col_b.button("Delete Completed"):
            st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
            st.rerun()
