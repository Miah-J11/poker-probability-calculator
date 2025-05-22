import streamlit as st
import poker_probability as pp

st.title("♠️ Poker Hand Probability Calculator ♥️")

st.write("""
Calculate the probability of getting different poker hands (e.g., pair, flush).
""")

num_simulations = st.slider("Number of simulations", 1000, 100000, 10000)
hand_type = st.selectbox("Select hand type", ["Pair", "Two Pair", "Flush"])

if st.button("Calculate Probability"):
    if hand_type == "Pair":
        prob = pp.simulate_probability(num_simulations)
    # (Extend for other hands)
    
    st.success(f"Probability of {hand_type}: **{prob*100:.2f}%**")
    st.write(f"Based on {num_simulations:,} simulations.")