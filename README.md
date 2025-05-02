# Gacha system
pull awards from the pool with pity system  

File:  
gacha_system.py: main program running the gacha system  
gacha_state.json: persist the program's state (e.g. current probabilities and awards count)  

Initialization:
1) Individualize your awards pool and probability in configuration part of gacha_system.py
2) If we need to adjust probability via Monte Carlo, set Monte_Carlo_test to True and individualize our Monte_Carlo_trial_number
3) After we finish adjusting probability, set Monte_Carlo_trial_number to 0 and run gacha_system.py
4) Set Monte_Carlo_test to False

Usage:
1) Enter the number of pulls in gacha_state.json
2) Make sure Monte_Carlo_test is False
3) Run gacha_system.py
4) Collect our received awards in gacha_state.json, by deleting the corresponding number of awards we collected
