import streamlit as st
from datetime import datetime


def render():
    st.header("Casa Shopping")

    # Initialize session state
    if "favorites" not in st.session_state:
        st.session_state.favorites = []

    # --- Item Search ---
    st.subheader("Search for Items")
    search_term = st.text_input("What are you looking for?", key="casa_search")

    if search_term:
        encoded = search_term.replace(" ", "+")
        encoded_url = search_term.replace(" ", "%20")

        st.markdown("#### Store Links")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"[Amazon](https://www.amazon.com/s?k={encoded})")
            st.markdown(f"[Costco](https://www.costco.com/CatalogSearch?dept=All&keyword={encoded})")
        with col2:
            st.markdown(f"[Target](https://www.target.com/s?searchTerm={encoded})")
            st.markdown(f"[Walmart](https://www.walmart.com/search?q={encoded})")
        with col3:
            st.markdown(f"[Instacart](https://www.instacart.com/store/search/{encoded_url})")

        # Add to favorites
        if st.button("Add to Favorites", key="add_fav_search"):
            if search_term not in st.session_state.favorites:
                st.session_state.favorites.append(search_term)
                st.success(f"Added '{search_term}' to favorites.")
            else:
                st.info("Already in favorites.")

    # --- Food Ordering ---
    st.divider()
    st.subheader("Food Ordering")
    food_search = st.text_input("What do you want to eat?", key="food_search")

    if food_search:
        encoded_food = food_search.replace(" ", "+")
        encoded_food_url = food_search.replace(" ", "%20")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"[DoorDash](https://www.doordash.com/search/store/{encoded_food_url}/)")
            st.markdown(f"[Uber Eats](https://www.ubereats.com/search?q={encoded_food})")
        with col2:
            st.markdown(f"[Postmates](https://postmates.com/search?q={encoded_food})")
            st.markdown(f"[Instacart](https://www.instacart.com/store/search/{encoded_food_url})")

    # --- Favorites ---
    st.divider()
    st.subheader("Favorites")

    if not st.session_state.favorites:
        st.info("No favorites yet. Search for something and add it.")
    else:
        for i, fav in enumerate(st.session_state.favorites):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{fav}**")
            with col2:
                if st.button("Remove", key=f"remove_fav_{i}"):
                    st.session_state.favorites.pop(i)
                    st.rerun()

    # --- Quick Add Favorite ---
    st.divider()
    new_fav = st.text_input("Add a favorite directly", key="direct_fav")
    if st.button("Add", key="add_direct_fav"):
        if new_fav and new_fav not in st.session_state.favorites:
            st.session_state.favorites.append(new_fav)
            st.rerun()
