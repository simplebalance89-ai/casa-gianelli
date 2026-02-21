import streamlit as st
from datetime import datetime


CATEGORIES = [
    "Produce",
    "Dairy & Eggs",
    "Meat & Seafood",
    "Pantry",
    "Snacks",
    "Beverages",
    "Frozen",
    "Bakery",
    "Baby",
    "Cleaning",
    "Personal Care",
    "Other",
]


def render():
    st.header("Grocery List")

    # Initialize session state
    if "grocery_items" not in st.session_state:
        st.session_state.grocery_items = []
    if "grocery_checked" not in st.session_state:
        st.session_state.grocery_checked = {}

    # --- Add Item Form ---
    with st.form("add_grocery", clear_on_submit=True):
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            item_name = st.text_input("Item")
        with col2:
            item_category = st.selectbox("Category", CATEGORIES)
        with col3:
            item_qty = st.text_input("Qty", value="1")

        if st.form_submit_button("Add Item"):
            if item_name:
                item_id = f"{item_name}_{datetime.now().timestamp()}"
                st.session_state.grocery_items.append({
                    "id": item_id,
                    "name": item_name,
                    "category": item_category,
                    "qty": item_qty,
                    "added": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                st.session_state.grocery_checked[item_id] = False
                st.rerun()

    # --- Summary ---
    total_items = len(st.session_state.grocery_items)
    checked_count = sum(1 for v in st.session_state.grocery_checked.values() if v)

    if total_items > 0:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Items", total_items)
        with col2:
            st.metric("Checked Off", checked_count)
        with col3:
            st.metric("Remaining", total_items - checked_count)

    # --- Clear Checked Button ---
    if checked_count > 0:
        if st.button(f"Clear {checked_count} Checked Items"):
            checked_ids = [k for k, v in st.session_state.grocery_checked.items() if v]
            st.session_state.grocery_items = [
                item for item in st.session_state.grocery_items
                if item["id"] not in checked_ids
            ]
            for cid in checked_ids:
                del st.session_state.grocery_checked[cid]
            st.rerun()

    # --- Display by Category ---
    if not st.session_state.grocery_items:
        st.info("Grocery list is empty. Add items above.")
    else:
        # Group items by category
        categories_present = {}
        for item in st.session_state.grocery_items:
            cat = item["category"]
            if cat not in categories_present:
                categories_present[cat] = []
            categories_present[cat].append(item)

        # Sort categories by the CATEGORIES list order
        sorted_cats = sorted(
            categories_present.keys(),
            key=lambda c: CATEGORIES.index(c) if c in CATEGORIES else 999
        )

        for cat in sorted_cats:
            items = categories_present[cat]
            st.subheader(f"{cat} ({len(items)})")

            for item in items:
                item_id = item["id"]
                col1, col2, col3, col4 = st.columns([0.5, 3, 1, 1])

                with col1:
                    is_checked = st.checkbox(
                        "done",
                        value=st.session_state.grocery_checked.get(item_id, False),
                        key=f"chk_{item_id}",
                        label_visibility="collapsed",
                    )
                    st.session_state.grocery_checked[item_id] = is_checked

                with col2:
                    if is_checked:
                        st.markdown(f"~~{item['name']}~~")
                    else:
                        st.write(item["name"])

                with col3:
                    st.write(f"x{item['qty']}")

                with col4:
                    if st.button("Remove", key=f"rm_{item_id}"):
                        st.session_state.grocery_items = [
                            i for i in st.session_state.grocery_items if i["id"] != item_id
                        ]
                        if item_id in st.session_state.grocery_checked:
                            del st.session_state.grocery_checked[item_id]
                        st.rerun()

    # --- Quick Add Common Items ---
    st.divider()
    st.subheader("Quick Add")
    quick_items = {
        "Milk": "Dairy & Eggs",
        "Eggs": "Dairy & Eggs",
        "Bread": "Bakery",
        "Bananas": "Produce",
        "Chicken": "Meat & Seafood",
        "Rice": "Pantry",
        "Water": "Beverages",
        "Diapers": "Baby",
        "Wipes": "Baby",
        "Formula": "Baby",
    }

    cols = st.columns(5)
    for i, (name, cat) in enumerate(quick_items.items()):
        with cols[i % 5]:
            if st.button(name, key=f"quick_{name}"):
                item_id = f"{name}_{datetime.now().timestamp()}"
                st.session_state.grocery_items.append({
                    "id": item_id,
                    "name": name,
                    "category": cat,
                    "qty": "1",
                    "added": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                st.session_state.grocery_checked[item_id] = False
                st.rerun()
