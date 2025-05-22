import numpy as np

#card ranks + suites
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦', '♣', '♠']

def create_deck():
    """Generate a standard 52-card deck."""
    return [f"{rank}{suit}" for rank in ranks for suit in suits]
    
def deal_hand(deck, n=5):
        return np.random.choice(deck, size=n, replace=False)
    
def is_pair(hand):
        ranks_in_hand=[card[:-1] for card in hand]
        return len(set(ranks_in_hand)) < len(ranks_in_hand)
    
def simulate_probability(num_simulations=10000):
    """Run Monte Carlo simulation to estimate probabilities."""
    deck = create_deck()
    pair_count = 0
    
    for _ in range(num_simulations):
        hand = deal_hand(deck)
        if is_pair(hand):
            pair_count += 1
    
    return pair_count / num_simulations