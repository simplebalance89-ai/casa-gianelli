import streamlit as st
from datetime import datetime


def render():
    st.header("Car Search")

    # Initialize session state
    if "car_picks" not in st.session_state:
        st.session_state.car_picks = []

    # --- Metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Budget", "$5,000 - $7,000")
    col2.metric("Type", "Toyota SUV/Truck")
    col3.metric("Purpose", "Short-term (couple months)")

    # --- Market Summary ---
    st.divider()
    st.subheader("Market Summary")
    st.markdown("""
- **Tacomas:** Hardest to find. SoCal truck tax brutal. Late 90s to mid-2000s, 200K+ miles.
- **4Runners:** Slightly better value. 1997-2006, $5,500-$6,900 range.
- **Highlanders:** Best bang for budget. Less truck tax, crossover pricing. Listings from $3,490.
- **RAV4s:** Reliable A-to-B option under $7K.
- **Best play:** 2002-2007 Highlander or 3rd-gen 4Runner. Buy, drive, sell for close to what you paid.
""")

    # --- Toyota Tacoma Listings ---
    st.divider()
    st.subheader("Toyota Tacoma - 7 Listings")
    tacoma_data = [
        ["~2000", "4-cyl 5-spd Single Cab", "N/A", "$5,800", "Sherman Oaks", "https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota+tacoma"],
        ["2001", "PreRunner", "N/A", "$6,500", "Los Angeles", "https://losangeles.craigslist.org/search/cta?query=toyota+tacoma"],
        ["1999", "4-cyl 5-spd", "N/A", "$6,300", "Fountain Valley", "https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota+tacoma"],
        ["1998", "Base", "238,460", "$4,988", "LA area", "https://www.cars.com/shopping/toyota-tacoma/los_angeles-ca/price-under-7000/"],
        ["2006", "Base", "244,328", "$6,902", "LA area", "https://www.cars.com/shopping/toyota-tacoma/los_angeles-ca/price-under-7000/"],
        ["1998", "Base (Surfside Green)", "N/A", "$6,975", "LA area", "https://www.cars.com/shopping/toyota-tacoma/los_angeles-ca/price-under-7000/"],
        ["2001", "Tacoma", "235,000", "$7,500", "Los Angeles", "https://offerup.com/explore/sck/ca/los_angeles/toyota-tacoma"],
    ]
    st.markdown("| Year | Trim | Miles | Price | Location | Source |")
    st.markdown("|------|------|-------|-------|----------|--------|")
    for row in tacoma_data:
        st.markdown(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | [Link]({row[5]}) |")
    st.info("Cars.com has **22 Tacomas under $7K** in LA - [View All](https://www.cars.com/shopping/toyota-tacoma/los_angeles-ca/price-under-7000/)")

    # --- Toyota 4Runner Listings ---
    st.divider()
    st.subheader("Toyota 4Runner - 5 Listings")
    fourrunner_data = [
        ["1997", "Limited 4X4", "N/A", "$5,750", "LA area", "https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota+4runner"],
        ["2002", "SR5", "N/A", "$5,500", "Central LA", "https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota+4runner"],
        ["2003", "4WD", "N/A", "$5,500", "Glendale", "https://losangeles.craigslist.org/search/cta?query=toyota+4runner"],
        ["2006", "SR5", "N/A", "$6,900", "Glendale", "https://losangeles.craigslist.org/search/cta?query=toyota+4runner"],
        ["2003", "SR5", "N/A", "$6,500", "LA area", "https://losangeles.craigslist.org/search/cta?query=toyota+4runner"],
    ]
    st.markdown("| Year | Trim | Miles | Price | Location | Source |")
    st.markdown("|------|------|-------|-------|----------|--------|")
    for row in fourrunner_data:
        st.markdown(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | [Link]({row[5]}) |")
    st.info("CarGurus has **4Runners starting at $5,995** in LA - [View All](https://www.cargurus.com/Cars/l-Used-Toyota-4Runner-Los-Angeles-d290_L2163)")

    # --- Toyota Highlander ---
    st.divider()
    st.subheader("Toyota Highlander - Best Value")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**TrueCar:** 744 listings in LA, starting at **$3,490**")
        st.markdown("[View on TrueCar](https://www.truecar.com/used-cars-for-sale/listings/toyota/highlander/location-los-angeles-ca/)")
    with col2:
        st.markdown("**CarGurus:** 460 listings, starting at **$4,250**")
        st.markdown("[View on CarGurus](https://www.cargurus.com/Cars/l-Used-Toyota-Highlander-Los-Angeles-d298_L2163)")

    # --- Search All Platforms ---
    st.divider()
    st.subheader("Search All Platforms")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Cars.com**")
        st.markdown("""
- [All Toyota <$7K LA](https://www.cars.com/shopping/toyota/los_angeles-ca/price-under-7000/)
- [Tacoma <$7K LA](https://www.cars.com/shopping/toyota-tacoma/los_angeles-ca/price-under-7000/)
- [4Runner <$10K LA](https://www.cars.com/shopping/toyota-4runner/los_angeles-ca/price-under-10000/)
- [Highlander <$10K LA](https://www.cars.com/shopping/toyota-highlander/los_angeles-ca/price-under-10000/)
""")
        st.markdown("**CarGurus**")
        st.markdown("""
- [4Runner LA](https://www.cargurus.com/Cars/l-Used-Toyota-4Runner-Los-Angeles-d290_L2163)
- [Tacoma LA](https://www.cargurus.com/Cars/l-Used-Toyota-Tacoma-Los-Angeles-d311_L2163)
- [Highlander LA](https://www.cargurus.com/Cars/l-Used-Toyota-Highlander-Los-Angeles-d298_L2163)
""")
        st.markdown("**TrueCar**")
        st.markdown("""
- [Trucks <$7K LA](https://www.truecar.com/used-cars-for-sale/listings/body-truck/price-below-7000/location-los-angeles-ca/)
""")
        st.markdown("**Autotrader**")
        st.markdown("""
- [Toyota by owner LA](https://www.autotrader.com/cars-for-sale/los-angeles-ca?sellerTypes=p)
""")

    with col2:
        st.markdown("**CARFAX**")
        st.markdown("""
- [Tacoma LA](https://www.carfax.com/Used-Toyota-Tacoma-Los-Angeles-CA_w641_c4914)
- [4Runner LA](https://www.carfax.com/Used-Toyota-4Runner-Los-Angeles-CA_w628_c4914)
- [Highlander LA](https://www.carfax.com/Used-Toyota-Highlander-Los-Angeles-CA_w632_c4914)
""")
        st.markdown("**Craigslist (by owner)**")
        st.markdown("""
- [Tacoma](https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota+tacoma)
- [4Runner](https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota+4runner)
- [All Toyota](https://losangeles.craigslist.org/search/cta?purveyor=owner&query=toyota)
""")
        st.markdown("**OfferUp**")
        st.markdown("""
- [Toyota Tacoma LA](https://offerup.com/explore/sck/ca/los_angeles/toyota-tacoma)
- [All Toyota LA](https://offerup.com/explore/sck/ca/los_angeles/toyota)
""")

    # --- Auctions in LA ---
    st.divider()
    st.subheader("Auctions in LA")
    st.markdown("""
- [**OPG (LAPD Impound)**](https://www.opgauction.com/) - Weekly, 500+ vehicles, photo ID only
- [**IAA Insurance Auto Auctions LA**](https://www.iaai.com/Locations/134)
- [**Copart Los Angeles**](https://www.copart.com/locations/los-angeles-ca-10)
- [**SCA Auctions LA**](https://sca.auction/locations/branch-ca-los-angeles-134) - 100% online
- [**Express Auto Auction**](https://expressautoauction.net) - No reserve, no minimum
- [**CHP Vehicle Sales**](https://www.chp.ca.gov/Pages/Auctions.aspx) - Gov surplus
""")

    # --- Familia Picks Form ---
    st.divider()
    st.subheader("Familia Picks")

    with st.form("save_car", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            year = st.text_input("Year")
            make_model = st.text_input("Make / Model")
        with col2:
            mileage = st.text_input("Mileage")
            price = st.text_input("Price")
        with col3:
            location = st.text_input("Location")
            source = st.selectbox("Source", [
                "Craigslist", "Cars.com", "CarGurus", "OfferUp",
                "Facebook", "Auction", "Other"
            ])

        link = st.text_input("Listing URL")
        notes = st.text_area("Notes", height=80)
        submitted = st.form_submit_button("Save Pick")

        if submitted and make_model:
            st.session_state.car_picks.append({
                "year": year,
                "make_model": make_model,
                "mileage": mileage,
                "price": price,
                "location": location,
                "source": source,
                "link": link,
                "notes": notes,
                "saved": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })
            st.success(f"Saved: {year} {make_model}")

    # --- Saved Picks ---
    st.divider()
    st.subheader("Saved Picks")

    if not st.session_state.car_picks:
        st.info("No saved picks yet. Use the form above to save vehicles the familia finds.")
    else:
        for i, car in enumerate(st.session_state.car_picks):
            label = f"{car['year']} {car['make_model']} - {car['price']}"
            with st.expander(label):
                st.write(f"**Mileage:** {car['mileage']}")
                st.write(f"**Location:** {car['location']}")
                st.write(f"**Source:** {car['source']}")
                if car["link"]:
                    st.markdown(f"[View Listing]({car['link']})")
                if car["notes"]:
                    st.write(f"**Notes:** {car['notes']}")
                st.caption(f"Saved: {car['saved']}")
                if st.button("Remove", key=f"remove_car_{i}"):
                    st.session_state.car_picks.pop(i)
                    st.rerun()
