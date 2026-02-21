"""Tab 15: GL Languages - Trilingual vocabulary cards + language coach chat."""
import streamlit as st
from utils.state import gl_age
from prompts.gl_languages import GL_LANG_PROMPT


VOCAB = {
    "Family": [
        ("Mom", "Mamma", "MAHM-mah", "Mamá", "mah-MAH"),
        ("Dad", "Papà", "pah-PAH", "Papá", "pah-PAH"),
        ("Baby", "Bambino", "bahm-BEE-noh", "Bebé", "beh-BEH"),
        ("Love", "Amore", "ah-MOR-eh", "Amor", "ah-MOR"),
    ],
    "Food": [
        ("Milk", "Latte", "LAHT-teh", "Leche", "LEH-cheh"),
        ("Water", "Acqua", "AH-kwah", "Agua", "AH-gwah"),
        ("Apple", "Mela", "MEH-lah", "Manzana", "mahn-SAH-nah"),
        ("Bread", "Pane", "PAH-neh", "Pan", "pahn"),
    ],
    "Animals": [
        ("Dog", "Cane", "KAH-neh", "Perro", "PEH-rroh"),
        ("Cat", "Gatto", "GAHT-toh", "Gato", "GAH-toh"),
        ("Bird", "Uccello", "oo-CHEL-loh", "Pájaro", "PAH-hah-roh"),
        ("Fish", "Pesce", "PEH-sheh", "Pez", "pehs"),
    ],
    "Colors": [
        ("Red", "Rosso", "ROHS-soh", "Rojo", "ROH-hoh"),
        ("Blue", "Blu", "bloo", "Azul", "ah-SOOL"),
        ("Green", "Verde", "VEHR-deh", "Verde", "VEHR-deh"),
        ("Yellow", "Giallo", "JAHL-loh", "Amarillo", "ah-mah-REE-yoh"),
    ],
    "Body": [
        ("Hand", "Mano", "MAH-noh", "Mano", "MAH-noh"),
        ("Eye", "Occhio", "OH-kyoh", "Ojo", "OH-hoh"),
        ("Nose", "Naso", "NAH-zoh", "Nariz", "nah-REES"),
        ("Mouth", "Bocca", "BOH-kah", "Boca", "BOH-kah"),
    ],
    "Nature": [
        ("Sun", "Sole", "SOH-leh", "Sol", "sohl"),
        ("Moon", "Luna", "LOO-nah", "Luna", "LOO-nah"),
        ("Rose", "Rosa", "ROH-zah", "Rosa", "ROH-sah"),
        ("Star", "Stella", "STEH-lah", "Estrella", "ehs-TREH-yah"),
    ],
}


def render():
    st.header("GL Languages")
    age = gl_age()
    st.caption(f"Trilingual vocabulary builder. GL is {age['months']:.1f} months old.")

    # Theme picker
    theme = st.radio(
        "Pick a theme",
        list(VOCAB.keys()),
        horizontal=True,
    )

    # Vocabulary cards
    words = VOCAB[theme]
    cols = st.columns(3)
    practiced_count = 0

    for i, (eng, ita, ita_pron, spa, spa_pron) in enumerate(words):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {eng}")
                st.markdown(f"**Italian:** {ita} (*{ita_pron}*)")
                st.markdown(f"**Spanish:** {spa} (*{spa_pron}*)")
                key = f"vocab_{theme}_{eng}"
                checked = st.checkbox("Practiced!", key=key)
                if checked and eng not in st.session_state.gl_vocab_practiced:
                    st.session_state.gl_vocab_practiced.append(eng)
                elif not checked and eng in st.session_state.gl_vocab_practiced:
                    st.session_state.gl_vocab_practiced.remove(eng)

    practiced_count = len(st.session_state.gl_vocab_practiced)
    st.success(f"Practiced **{practiced_count}** words this session")

    st.divider()

    # Chat section
    with st.expander("Ask Language Buddy"):
        for msg in st.session_state.gl_lang_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        col1, col2 = st.columns([5, 1])
        with col1:
            user_msg = st.text_input(
                "Ask about languages...",
                key="gl_lang_chat_input",
                label_visibility="collapsed",
            )
        with col2:
            if st.button("Send", key="gl_lang_send"):
                if user_msg:
                    st.session_state.gl_lang_messages.append({"role": "user", "content": user_msg})
                    st.rerun()

        if st.session_state.gl_lang_messages and st.session_state.gl_lang_messages[-1]["role"] == "user":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        from utils.ai_client import chat
                        reply = chat(GL_LANG_PROMPT, st.session_state.gl_lang_messages)
                        st.markdown(reply)
                        st.session_state.gl_lang_messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")
