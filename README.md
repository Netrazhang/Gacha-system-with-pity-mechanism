# self-rewarding-gacha-system
pull awards from the pool with pity system  

File:  
gacha_system.py: main program running the gacha system  
gacha_state.json: persist the program's state (e.g. current probabilities and awards count)  

Usage:
1) Individualize your awards pool and probability in configuration part of gacha_system.py
2) If you chhoose to finish 1), delete gacha_state.json and run gacha_system.py to create corresponding gacha_state.json.
3) Enter the number of pulls in gacha_state.json
4) Run gacha_system.py
5) Check your received awards in gacha_state.json
