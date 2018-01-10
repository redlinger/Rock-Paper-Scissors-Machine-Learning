# Rock-Paper-Scissors-Machine-Learning
Rock Paper Scissors with Machine Learning

RPS_random.py:
Human vs. Computer (Random)
Computer uses Python's psuedo-random number generator to choose rock, paper,
or scissors. The code also keeps track of the score.


RPS_svm.py
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
