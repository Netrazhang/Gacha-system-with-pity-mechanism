import random
import json
import os
import sys
from collections import defaultdict

# Configuration
state_file = 'gacha_state.json'
initial_award_probability = {
    'Thanks for participating': 0.6,
    'Third Prize': 0.25,
    'Second Prize': 0.1,
    'First Prize': 0.04,
    'Grand Prize': 0.01
}
awards = list(initial_award_probability.keys())
big_awards = ['First Prize', 'Grand Prize']
# Set up the defaultdict with all initial keys and value 0
award_received = defaultdict(int, {key: 0 for key in initial_award_probability})
init_state = {'award_probability': initial_award_probability, 'award_received': award_received, 'pull_count': 0}
initialize_system = False

# Load state from json file
def load_state(file):
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return init_state

# Save state to json file
def save_state(state, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

# Compute award probability based on current probability list:
def generate_next_award_probability(prob_dict):
    prob_sum = 0
    idx = len(prob_dict)
    while(idx > 0):
        idx -= 1
        if prob_sum < 1:
            prob_dict[awards[idx]] = min(prob_dict[awards[idx]]*1.1, prob_dict[awards[idx]]+0.01, 1-prob_sum)
            prob_sum += prob_dict[awards[idx]]
        else:
            prob_dict[awards[idx]] = 0
    return prob_dict

# Main draw logic
def draw_award(state):
    probs = state['award_probability']
    for _ in range(state['pull_count']):
        result = random.choices(list(probs.keys()), weights=list(probs.values()))[0]
        # add result to award_received
        print(f'Draw result: {result}')
        state['award_received'][result] += 1
        if result in big_awards:
            # initialize state
            state['award_probability'] = initial_award_probability
        else:
            generate_next_award_probability(state['award_probability'])
        state['pull_count'] -= 1


def main():
    # Get the folder where the current .py file resides
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Set it as the current working directory
    os.chdir(script_dir)
    # Load state from json file under the same folder
    state = load_state(state_file)
    print('Loaded state.')
    # Draw cards!
    draw_award(state)
    print('Awards received.')
    # Save to json file
    if initialize_system == True:
        state = init_state
        print('Gacha system initialized.')
    save_state(state, state_file)
    print('Updated state.')


if __name__ == '__main__':
    main()