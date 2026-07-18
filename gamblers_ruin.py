import numpy as np 
import random 
import pandas as pd 
import matplotlib.pyplot as plt 

# matplotlib parameters 
plt.rcParams['figure.figsize'] = (12,8)
plt.rcParams.update({'font.size': 14})

def gamblers_ruin():
    gambling_money = 50
    gambling_goal  = 100
    gambling_simulations = []
    
    while gambling_money in range(1, gambling_goal):
        bet_size = 1
        w_or_l = random.randrange(-1, 2, 2)
        gambling_money += bet_size * w_or_l
        gambling_simulations.append(gambling_money)
    return gambling_simulations

plt.plot(gamblers_ruin())
plt.yticks(np.arange(-20, 120, 10))
plt.axhline(y=0, color='r', linestyle='-')
plt.axhline(y=100, color='black', linestyle='-')
plt.xlabel('Number of bets')
plt.ylabel('Winnings')
plt.title('Gambling Simulation')
# plt.show()

def prob_of_ruin(gambling_goal, initial_gambling_money):
    return (gambling_goal - initial_gambling_money) / gambling_goal

sim_list = []
while len(sim_list) < 450:
    sim_list.append(gamblers_ruin()[-1])
    
print(np.mean(sim_list))
