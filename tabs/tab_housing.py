import streamlit as st
from datetime import datetime


def render():
    st.header("Housing Search")

    # Initialize session state
    if "housing_picks" not in st.session_state:
        st.session_state.housing_picks = []

    # --- Metrics ---
    c1, c2, c3 = st.columns(3)
    c1.metric("Target Move-In", "March 1, 2026")
    c2.metric("Duration", "3-6 months")
    c3.metric("Bedrooms", "3+")

    st.divider()

    # --- Location Toggle ---
    location = st.radio("Search Area", ["Palm Springs", "Big Bear"], horizontal=True)

    # =====================================================================
    # PALM SPRINGS
    # =====================================================================
    if location == "Palm Springs":
        st.subheader("Palm Springs / Coachella Valley")

        # Requirements
        st.markdown("**Requirements:** Furnished, A/C, Washer/Dryer, WiFi, Pool, Baby friendly")
        st.markdown("**Budget:** Rent TBD | Utilities ~$200-400/mo | Internet ~$80-100/mo")
        st.markdown("**Family:** Peter, Gladys, 3 kids")

        st.divider()

        # --- Search All Platforms ---
        st.subheader("Search All Platforms")
        st.markdown("""
| Platform | Area | Filter | Link |
|----------|------|--------|------|
| Airbnb | Palm Springs | 3BR+, Monthly, Mar-Jun | [Search](https://www.airbnb.com/s/Palm-Springs--CA/homes?adults=2&children=3&checkin=2026-03-01&checkout=2026-06-01&min_bedrooms=3&monthly_stay=true) |
| VRBO | Palm Springs | 3BR+, Monthly, Mar-Jun | [Search](https://www.vrbo.com/search?destination=Palm+Springs%2C+CA&adults=2&children=3&startDate=2026-03-01&endDate=2026-06-01&minBedrooms=3) |
| Furnished Finder | Palm Springs | Furnished rentals | [Search](https://www.furnishedfinder.com/housing/Palm-Springs-California) |
| Zillow | Palm Springs | 3BR+ Furnished Rentals | [Search](https://www.zillow.com/palm-springs-ca/rentals/) |
| Apartments.com | Palm Springs | 3BR Furnished | [Search](https://www.apartments.com/palm-springs-ca/furnished/3-bedrooms/) |
| Craigslist | Palm Springs | 3BR+ Apartments | [Search](https://palmsprings.craigslist.org/search/apa?min_bedrooms=3&availabilityMode=0) |
| Facebook | Palm Springs | Property Rentals | [Search](https://www.facebook.com/marketplace/palmsprings/propertyrentals) |
""")

        st.divider()

        # --- Expand to Nearby Areas ---
        st.subheader("Expand to Nearby Areas")
        st.markdown("""
| Platform | Area | Link |
|----------|------|------|
| Airbnb | Palm Desert | [Search](https://www.airbnb.com/s/Palm-Desert--CA/homes?adults=2&children=3&min_bedrooms=3&monthly_stay=true) |
| Airbnb | Rancho Mirage | [Search](https://www.airbnb.com/s/Rancho-Mirage--CA/homes?adults=2&children=3&min_bedrooms=3&monthly_stay=true) |
| Airbnb | La Quinta | [Search](https://www.airbnb.com/s/La-Quinta--CA/homes?adults=2&children=3&min_bedrooms=3&monthly_stay=true) |
| Airbnb | Cathedral City | [Search](https://www.airbnb.com/s/Cathedral-City--CA/homes?adults=2&children=3&min_bedrooms=3&monthly_stay=true) |
| Zillow | Palm Desert Rentals | [Search](https://www.zillow.com/palm-desert-ca/rentals/) |
| Zillow | Rancho Mirage Rentals | [Search](https://www.zillow.com/rancho-mirage-ca/rentals/) |
| Zillow | La Quinta Rentals | [Search](https://www.zillow.com/la-quinta-ca/rentals/) |
| Craigslist | Palm Desert | [Search](https://palmsprings.craigslist.org/search/apa?min_bedrooms=3&query=palm+desert) |
""")

    # =====================================================================
    # BIG BEAR
    # =====================================================================
    else:
        st.subheader("Big Bear Lake")

        # Requirements
        st.markdown("**Requirements:** Furnished, NOT Airbnb (monthly rental), Heating, Washer/Dryer, WiFi, Garage, Baby friendly")
        st.markdown("**Budget:** $2,000-3,800/mo | Utilities included preferred | Internet ~$80-100/mo")
        st.markdown("**Family:** Peter, Gladys, 3 kids")

        st.divider()

        # --- Search All Platforms ---
        st.subheader("Search All Platforms")
        st.markdown("""
| Platform | Area | Link |
|----------|------|------|
| Furnished Finder | Big Bear | [Search](https://www.furnishedfinder.com/housing/Big-Bear-Lake-California) |
| Zillow | Big Bear Lake | [Search](https://www.zillow.com/big-bear-lake-ca/rentals/) |
| Zillow | Big Bear City | [Search](https://www.zillow.com/big-bear-city-ca/rentals/) |
| Trulia | Big Bear Lake | [Search](https://www.trulia.com/for_rent/Big_Bear_Lake,CA/) |
| Apartments.com | Big Bear | [Search](https://www.apartments.com/big-bear-lake-ca/furnished/) |
| Craigslist | Inland Empire | [Search](https://inlandempire.craigslist.org/search/apa?query=big+bear) |
| Facebook | Big Bear | [Search](https://www.facebook.com/marketplace/bigbearlake/propertyrentals) |
| HotPads | Big Bear Lake | [Search](https://hotpads.com/big-bear-lake-ca/houses-for-rent) |
""")

        st.divider()

        # --- Property Managers ---
        st.subheader("Big Bear Property Managers")
        st.markdown("""
| Company | Phone | Website |
|---------|-------|---------|
| Big Bear Cool Cabins | (909) 866-3143 | [coolcabins.com](https://www.coolcabins.com) |
| Big Bear Vacations | (909) 585-7373 | [bigbearvacations.com](https://www.bigbearvacations.com) |
| RSVacations | (909) 866-5683 | [rsvacations.com](https://www.rsvacations.com) |
| Gold Rush Resort Rentals | (800) 967-1674 | [bigbearresort.com](https://www.bigbearresort.com) |
""")

    # =====================================================================
    # QUESTIONS TO ASK (both locations)
    # =====================================================================
    st.divider()
    with st.expander("Questions to Ask Every Listing"):
        st.markdown("""
1. Total monthly cost (rent + utilities + fees)?
2. Security deposit?
3. Minimum stay? Flexible on 3-6 months?
4. Pet policy?
5. Internet speed?
6. Parking (2 cars)?
7. Pool access? (Palm Springs) / Fireplace? (Big Bear)
8. Baby/child friendly?
""")

    # =====================================================================
    # FAMILIA PICKS FORM
    # =====================================================================
    st.divider()
    st.subheader("Familia Picks")

    with st.form("save_housing_pick", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            address = st.text_input("Address")
            source = st.selectbox("Source", [
                "Airbnb", "VRBO", "Furnished Finder", "Zillow",
                "Craigslist", "Facebook", "Other"
            ])
            price = st.text_input("Price / Month")
        with col2:
            beds = st.selectbox("Bedrooms", ["3", "4", "5+"])
            link = st.text_input("Link")
        notes = st.text_area("Notes", height=80)
        submitted = st.form_submit_button("Save Pick")

        if submitted and address:
            st.session_state.housing_picks.append({
                "address": address,
                "source": source,
                "price": price,
                "beds": beds,
                "link": link,
                "notes": notes,
                "saved": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "location": location,
            })
            st.success(f"Saved: {address}")

    # --- Saved Picks ---
    st.divider()
    st.subheader("Saved Picks")

    if not st.session_state.housing_picks:
        st.info("No saved picks yet. Use the form above to save listings.")
    else:
        for i, pick in enumerate(st.session_state.housing_picks):
            with st.expander(f"{pick['address']} - {pick.get('price', 'N/A')}/mo ({pick.get('source', 'N/A')})"):
                st.write(f"**Location:** {pick['location']}")
                st.write(f"**Bedrooms:** {pick['beds']}")
                st.write(f"**Source:** {pick.get('source', 'N/A')}")
                if pick.get("link"):
                    st.markdown(f"[View Listing]({pick['link']})")
                if pick.get("notes"):
                    st.write(f"**Notes:** {pick['notes']}")
                st.caption(f"Saved: {pick['saved']}")
                if st.button("Remove", key=f"remove_housing_{i}"):
                    st.session_state.housing_picks.pop(i)
                    st.rerun()
