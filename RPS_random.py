# -*- coding: utf-8 -*-
"""
Rock, Paper, Scissors
Human vs. Computer (Random)

Computer uses Python's psuedo-random number generator to choose rock, paper,
or scissors. The code also keeps track of the score.

"""

import random
import time

# valid fists
fists = ['rock', 'paper', 'scissors']
# dominant fists correspond to the fist they dominant
dom_fists = ['paper', 'scissors', 'rock']

# variables to keep track of score
comp_wins = 0
comp_loss = 0
ties = 0

# BEGIN GAME ##################################################################
print('Rock, Paper, Scissors! Enter q to quit.' )

# continue playing until player wants to quit
while True:
    # get input from huuuuman
    hum_fist = input('Enter "rock", "paper", or "scissors": ')    
    
    # end is user wants to quit
    if hum_fist == 'q':
        print('Final Score:')
        print('Human', 'Computer', 'Ties', sep='\t')
        print(' %s \t %s \t \t %s' % (comp_loss, comp_wins, ties))
        break
    
    # if input is invalid, report error
    if hum_fist not in fists:
        print('This is rock, paper, scissors. Not rock, paper, %s!' % hum_fist)
    
    # if input is valid, then see who is the winner
    else:
        # randomly draw number 0 (rock), 1 (paper), 2 (scissors)
        draw = random.randrange(0,3)
        comp_fist= fists[draw]
        # report what was chosen
        print('You: %s' % hum_fist)
        print('Me: %s' % comp_fist)
        # report if there is a tie
        if hum_fist == comp_fist:
            print('Tie! We both chose %s.' % comp_fist)
            ties += 1
            
        else:
            # report winner
            if hum_fist == dom_fists[draw]:
                print('You win! %s beats %s' % (hum_fist, comp_fist))
                comp_loss += 1
            else:
                print('I win! %s beats %s' % (comp_fist, hum_fist))
                comp_wins += 1
                
        # short break so slow human can read and then report score
        time.sleep(2)
        print('Score:')
        print('Human', 'Computer', 'Ties', sep='\t')
        print(' %s \t %s \t \t %s' % (comp_loss, comp_wins, ties))
