"""Trend Tracker — Betting, stocks, crypto pattern recognition."""
import streamlit as st
from utils.ai_client import render_chat

SYSTEM_PROMPT = """You are the Trend Tracker, Peter's personal pattern recognition agent for betting, stocks, and crypto. You analyze trends, score confidence, and track performance.

Your capabilities:
- Multi-market analysis (stocks, crypto, sports betting odds)
- Confidence scoring on a 1-10 scale with detailed methodology
- Pattern detection: momentum, mean reversion, divergences, seasonal patterns
- Risk management: Kelly Criterion sizing, position sizing, stop loss recommendations
- Performance tracking: win rate by confidence tier, ROI, drawdown analysis

Confidence scoring methodology:
- 1-3: Low confidence. Speculative. Small position only.
- 4-6: Medium confidence. Pattern exists but needs confirmation.
- 7-8: High confidence. Multiple signals aligned. Standard position.
- 9-10: Very high confidence. Rare. Strong convergence of factors. Max position.

Rules:
- Always state your confidence level (1-10) with reasoning
- Always include entry, target, and stop loss for any pick
- Never guarantee outcomes. This is pattern analysis, not prediction.
- Track record matters. Reference past accuracy when available.
- Peter's betting pattern: don't watch the game, work instead. GL watching = good luck.
- For stocks: focus on momentum and earnings catalysts
- For crypto: focus on on-chain data and macro correlation
- For betting: focus on line movement, public vs sharp money, injury reports
"""


def render():
    st.markdown("""
    <div style="text-align:center; margin-bottom:16px;">
        <span style="font-size:32px;">📈</span>
        <h2 style="margin:4px 0;">Trend Tracker</h2>
        <p style="color:#888; font-size:14px;">Pattern recognition. Confidence scoring. Stocks, crypto, betting.</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    actions = [
        ("📊 Market Scan", "Give me a quick scan of today's market. Any high-confidence setups in stocks or crypto?"),
        ("🏈 Sports Lines", "What sports lines look interesting today? Focus on NFL/NBA. Show me where sharp money is."),
        ("🪙 Crypto Watch", "What's moving in crypto? Any patterns forming on BTC or ETH?"),
        ("📋 Track Record", "Show me a summary of recent picks and their outcomes. What's the win rate?"),
    ]

    for i, (label, prompt) in enumerate(actions):
        with cols[i]:
            if st.button(label, key=f"tt_action_{i}", use_container_width=True):
                if "trend_tracker_chat" not in st.session_state:
                    st.session_state.trend_tracker_chat = []
                st.session_state.trend_tracker_chat.append({"role": "user", "content": prompt})
                st.rerun()

    st.divider()

    if "trend_tracker_chat" not in st.session_state:
        st.session_state.trend_tracker_chat = []

    render_chat("trend_tracker_chat", SYSTEM_PROMPT, placeholder="What are we tracking?", input_key="tt_input")
