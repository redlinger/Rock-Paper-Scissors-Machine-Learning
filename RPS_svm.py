# -*- coding: utf-8 -*-
"""

Rock, Paper, Scissors
Play vs. Computer (SVM)

Computer uses Support Vector Machine (SVM) to choose rock, paper, or scissors.
The sklearn SVM Support Vector Classification (SVC) model with grid search 
uses the last 3 rounds of data to predict what choice the human player will 
make next. The computer then chooses whatever will beat what the human is predicted
to do. The data from the 3 prior rounds are the players choices (i.e., rock, 
paper, scissors) and whether the human won, lost, or tied. Grid search is done
on the SVC penalty parameter and coefficient for rbf kernel.

The SVC initially uses a text file of human player history to make the prediction.
As you play more, your play history is incorporated into the SVC fit and prediction.
At the end, when you enter q, your data is saved back to the text file.

Good luck humans!

"""

import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV

# load data of human player history from text file
# col 1 is round number / observation
# col 2-5: human choice in last 4 rounds
#     h1= human's play in last round, h2= human's play in 2 rounds back, etc.
#     rock=0, paper=1, scissors=2
# col 6-9: winner in last 4 rounds 
#     hw= 1 if human won; = 0 if human lost, = 2 if tie
play_hist = np.genfromtxt('rps_history.txt', delimiter=",", dtype=int, skip_header=1)

# current round- numbering started at 0
round_crnt = np.shape(play_hist)[0]

# valid fists
fists = ['rock', 'paper', 'scissors']
# dominant fists correspond to the fist they dominant
dom_fists = ['paper', 'scissors', 'rock']

# score keeping variables
comp_wins = 0
comp_loss = 0
ties = 0

# initial SVM estiamted from existing data
# penalty parameter
#
params = {'C': np.logspace(-2,5,10),'gamma': np.logspace(-5,3,10)}
svc= svm.SVC(kernel='rbf')
model = GridSearchCV(svc, params)

# fit data to full history
# X_hist= 3 prior round plays and wins for all rounds played
X_hist = np.c_[play_hist[:, 2:5], play_hist[:, 6:]]
y_hist = play_hist[:, 1]

model.fit(X_hist,y_hist)

# predict human's next choice
# X_now= 3 previous rounds plays and wins
X_now = np.c_[play_hist[-1:, 2:5], play_hist[-1:, 6:]]
hum_fist_pred = model.predict(X_now)[0]

# computer chooses fist that beats the predicted human fist
comp_fist = dom_fists[hum_fist_pred]


# BEGIN GAME ##################################################################
print('Rock, Paper, Scissors! Enter q to quit.' )
print('Good Luck Human!')

# continue playing until player wants to quit
while True:
    
    # get input from huuuuman
    hum_fist = input('Enter "rock", "paper", or "scissors": ')    
    
    # end is user wants to quit
    if hum_fist == 'q':
        #print score
        print('Final Score:')
        print('Human', 'Computer', 'Ties', sep='\t')
        print(' %s \t %s \t \t %s' % (comp_loss, comp_wins, ties))
        # save data to text file
        np.savetxt('rps_history.txt', play_hist, delimiter=",", fmt="%i", newline="\r\n",
                   header='n,h1,h2,h3,h4,hw1,hw2,hw3,hw4')
        break
    
    # if input is invalid, report error
    if hum_fist not in fists:
        print('This is rock, paper, scissors. Not rock, paper, %s!' % hum_fist)
    
    # if input is valid, then see who is the winner
    else:
        # report what was chosen
        print('Human: %s' % hum_fist)
        print('Computer: %s' % comp_fist)
        # report if there is a tie
        if hum_fist == comp_fist:
            print('Tie! We both chose %s.' % hum_fist)
            ties += 1
            hum_win = 2 # =0 if hum lost, =1 if hum won, =2 if tie
            
        else:
            # report winner
            if hum_fist != fists[hum_fist_pred]:
                print('You win! %s beats %s' % (hum_fist, comp_fist))
                comp_loss += 1
                hum_win = 1  # =0 if hum lost, =1 if hum won, =2 if tie
                
            else:
                print('I win! %s beats %s' % (comp_fist, hum_fist))
                comp_wins += 1
                hum_win = 0 # =0 if hum lost, =1 if hum won, =2 if tie
                
        # fit data to full history
        # X_hist= 3 prior round plays and wins for all rounds played
        X_hist = np.c_[play_hist[:, 2:5], play_hist[:, 6:]]
        y_hist = play_hist[:, 1]
        model.fit(X_hist,y_hist)
        # predict human's next choice
        # X_now= 3 previous rounds plays and wins
        X_now = np.c_[play_hist[-1:, 2:5], play_hist[-1:, 6:]]
        hum_fist_pred = model.predict(X_now)[0]
        # computer chooses fist that beats the predicted human fist
        comp_fist = dom_fists[hum_fist_pred]
        
        # append data to history:
        # current round number, last round hum fist, hum fists from 3 prior round
        # last round human win, wins from 3 prior rounds
        prior_hist = play_hist[(round_crnt-1),1:4]
        prior_wins = play_hist[(round_crnt-1),5:8]
        play_hist = np.r_[play_hist, [np.concatenate([np.array([round_crnt]), 
                                             np.array([fists.index(hum_fist)]), 
                                             prior_hist, 
                                             np.array([hum_win]),
                                             prior_wins], axis=0)]]
        
        # increment round number
        round_crnt += 1
        
        #print score
        print('Score:')
        print('Human', 'Computer', 'Ties', sep='\t')
        print(' %s \t %s \t \t %s' % (comp_loss, comp_wins, ties))
        