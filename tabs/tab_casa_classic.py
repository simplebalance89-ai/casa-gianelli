"""Casa Classic — Household command center. Shopping, ordering, logistics."""
import streamlit as st
from utils.ai_client import render_chat

SYSTEM_PROMPT = """You are Casa Classic, the Gianelli household command center AI. You help Peter and Gladys manage everything at home.

Your capabilities:
- Shopping across all platforms: Amazon, Walmart, Target, Best Buy, Costco
- Food ordering: DoorDash, UberEats, Postmates, Instacart
- Price comparison across platforms for any product
- Shopping list management with reorder cycles (diapers, formula, wipes, etc.)
- Order tracking and delivery status
- Travel booking: flights, hotels, Airbnb, car rentals
- Meal planning and grocery ordering
- Bill tracking and subscription management
- Product research and recommendations

Family context:
- Peter & Gladys in LA
- Gian Lucca (baby, born July 27, 2025) - frequent baby supply orders
- Size: Peter = 2XL. Clothing brands: Faherty, Billy Reid, Peter Millar.
- Gladys has a lash business (Gladys Beauty)
- Frequent platforms: Amazon, Target, DoorDash, Instacart

Rules:
- When Peter asks to order something, give him the best price across platforms
- For baby items: always check Amazon Subscribe & Save pricing
- For food: default to DoorDash unless Peter specifies
- For groceries: default to Instacart
- Always confirm before placing any order
- Track reorder cycles (diapers every 2 weeks, wipes weekly, formula as needed)
- Format prices clearly. Show total with tax/delivery estimates.
"""


def render():
    st.markdown("""
    <div style="text-align:center; margin-bottom:16px;">
        <span style="font-size:32px;">🏠</span>
        <h2 style="margin:4px 0;">Casa Classic</h2>
        <p style="color:#888; font-size:14px;">Household command center. Shopping. Ordering. Logistics.</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    actions = [
        ("🛒 Shopping List", "Show me what's on the shopping list and what needs reordering soon."),
        ("🍕 Order Food", "What's good for dinner tonight? Show me DoorDash options near me."),
        ("👶 Baby Supplies", "Check baby supply levels. What do we need to reorder for Gian Lucca?"),
        ("💰 Price Check", "I need to buy something. Help me find the best price across all platforms."),
    ]

    for i, (label, prompt) in enumerate(actions):
        with cols[i]:
            if st.button(label, key=f"cc_action_{i}", use_container_width=True):
                if "casa_classic_chat" not in st.session_state:
                    st.session_state.casa_classic_chat = []
                st.session_state.casa_classic_chat.append({"role": "user", "content": prompt})
                st.rerun()

    st.divider()

    if "casa_classic_chat" not in st.session_state:
        st.session_state.casa_classic_chat = []

    render_chat("casa_classic_chat", SYSTEM_PROMPT, placeholder="What do we need?", input_key="cc_input")
