# 1 - 50 house wins
# 51 - 99 user wins
# 100 house wins


import random

def roll_dice():
    roll = random.randint(1,100)
    return roll

# Montecarlo simulation

win_lose = dict()
roll = 0

number_of_sim = 100000
for i in range(number_of_sim):
    roll = roll_dice()
    if roll == 100:
        win_lose['lose'] = win_lose.get('lose',0) + 1
    elif roll <= 50:
        win_lose['lose'] = win_lose.get('lose',0) + 1
    elif roll > 50:
        win_lose['win'] = win_lose.get('win',0) + 1

print win_lose

print ('Wins %', float(win_lose['win'])  / number_of_sim  * 100 )
print ('Lose %', float(win_lose['lose'])  / number_of_sim  * 100)
