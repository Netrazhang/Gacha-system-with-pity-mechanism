# self-rewarding-gacha-system
# pull awards from the pool with pity system


File:
gacha_system.py: main program running the gacha system
system_state.json: persist the program's state (e.g. current probabilities and fail count) 

Function:
gacha: takes in number of pulls, read the file
generate_award_probability: generate the weight of each awards based on initial_award_probability and 


Variable:
initial_award_probability: a dictionary with keys as awards, values as probability of awards
big_award: a list which is supposed to be a sublist of initial_award_probability's keys. Award probability will be increased until receiving one big award.
