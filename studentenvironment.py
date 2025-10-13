# CS 440 Multi-Armed Bandit Assignment
# (C) 2017 Travis Mandel

#These imports should be sufficient
import random
import math
import distributions as dists
import environments as envs

#Write a comment explaining why UCB-0.01 must always be better than UCB-1, or
# a comment explaining your counterexample environment
class StudentEnv(envs.MABEnvironment):
    def __init__(self):
        #YOUR CODE HERE
        pass #remove once implemented

    def pull(self,arm):
        #YOUR CODE HERE
        pass #remove once implemented

    def reset(self):
        #YOUR CODE HERE
        return False #Change to return True once implemented
    
    def getNumArms(self):
        #YOUR CODE HERE
        pass #remove once implemented
 
    def getMinReward(self):
        #YOUR CODE HERE
        pass #remove once implemented
		
    def getMaxReward(self):
        #YOUR CODE HERE
        pass #remove once implemented
