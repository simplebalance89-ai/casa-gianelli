"""Music Discovery tab - Mood-based recommendations, core artists, new explores."""
import streamlit as st


def render():
    st.header("Music Discovery")
    st.caption("Find tracks by mood, meaning, and connection.")

    moods = {
        "Release": [
            ("070 Shake", "Guilty Conscience", "Dark, ethereal, cathartic"),
            ("Papa Roach", "Last Resort", "The rage years"),
            ("MGK", "5:3666", "Hotel Diablo darkness"),
        ],
        "Land / Calm": [
            ("Sampha", "(No One Knows Me) Like the Piano", "Raw, intimate, just keys and soul"),
            ("Hozier", "Take Me to Church", "Soul music for empaths"),
            ("Dijon", "Rodeo Clown", "Genre-fluid, raw"),
        ],
        "Missing Mom": [
            ("Fleetwood Mac", "Landslide", "Phantasma playlist"),
            ("Meat Loaf", "I'd Do Anything for Love", "Mom's era"),
            ("Stevie Nicks", "Edge of Seventeen", "Phantasma playlist"),
        ],
        "Brotherhood": [
            ("Twenty One Pilots", "My Blood", "For Jimmy. Brothers."),
            ("Papa Roach", "Blood Brothers", "The bond"),
            ("Mike Posner", "Be As You Are", "Raw honesty, no mask"),
        ],
        "Gratitude / Light": [
            ("MGK", "sun to me", "Found the light. For Gladys."),
            ("SAINt JHN", "The Best Part of Life", "For Gian Lucca"),
            ("MARINA", "Butterfly", "Theatrical transformation"),
        ],
        "Focus / Work": [
            ("Various", "Melodic House Mix", "Progressive, no lyrics"),
            ("Labrinth", "Euphoria Soundtrack", "Cinematic soul"),
            ("Mk.gee", "Sal", "Guitar-driven, dreamy"),
        ],
        "Decompress": [
            ("070 Shake", "Guilty Conscience", "1. Release"),
            ("Sampha", "No One Knows Me Like the Piano", "2. Land"),
            ("Fleetwood Mac", "Phantasma Rotation", "3. Mom"),
            ("Twenty One Pilots", "My Blood", "4. Brothers"),
            ("Mike Posner", "Be As You Are", "5. Close"),
        ],
    }

    selected_mood = st.radio(
        "What do you need?",
        list(moods.keys()),
        horizontal=True,
    )

    st.subheader(f"Tracks for: {selected_mood}")
    tracks = moods[selected_mood]
    for artist, track, vibe in tracks:
        search_query = f"{artist} {track}".replace(" ", "%20")
        spotify_url = f"https://open.spotify.com/search/{search_query}"
        with st.expander(f"{artist} \u2014 {track}"):
            st.markdown(f"*{vibe}*")
            st.markdown(f"[{chr(9654)} Play on Spotify]({spotify_url})")

    st.divider()

    # New Artists to Explore
    st.subheader("New Artists to Explore (2026)")
    new_artists = [
        ("Sampha", "(No One Knows Me) Like the Piano", "Raw, intimate"),
        ("070 Shake", "Guilty Conscience", "Dark, ethereal"),
        ("Dijon", "Rodeo Clown", "Genre-fluid, raw"),
        ("Obongjayar", "Message in a Hammer", "UK soul"),
        ("Mk.gee", "Sal", "Guitar-driven, dreamy"),
        ("Jean Dawson", "Houston", "Genre-bending, cinematic"),
        ("SAINt JHN", "The Best Part of Life", "Dark R&B"),
    ]
    for artist, track, vibe in new_artists:
        st.markdown(f"**{artist}** \u2014 {track} *({vibe})*")

    st.divider()

    # Core Artists
    st.subheader("Core Artists")
    st.markdown("""
| Artist | Why They Matter |
|--------|-----------------|
| MGK | Lived the same darkness-to-light journey |
| Twenty One Pilots | Emotional depth for empaths |
| Blue October | Wrote the Wilson brothers' story |
| Papa Roach | The rage years, losing mom |
| Hozier | Soul music for empaths |
| Mike Posner | Raw honesty, no mask |
| Labrinth | Euphoria soundtrack, cinematic soul |
| MARINA | Theatrical transformation, butterfly |
    """)

    st.divider()

    # Streaming Services
    st.subheader("Streaming Services")
    col1, col2, col3 = st.columns(3)
    col1.markdown("**[Spotify](https://open.spotify.com)**")
    col2.markdown("**[Tidal](https://listen.tidal.com)**")
    col3.markdown("**[1001Tracklists](https://www.1001tracklists.com)** (DJ mixes, track IDs)")
