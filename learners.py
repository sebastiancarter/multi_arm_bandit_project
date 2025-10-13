# CS 440 Multi-Armed Bandit Assignment
# (C) 2017 Travis Mandel

#These imports should be sufficient
import random
import math
import environments as envs
import distributions as dists

# Interface (abstract) for multiarmed bandit learners
# Don't change this
class MABLearner(object):

    # Re-initializes the MAB with a given MABEnvironment
    # Returns True if initialization was successful, False otherwise
    def initWithEnvironment(self,env):
        pass

    #Chooses an arm to pull based on all the rewards processed so far
    # Arms are represented as integers, so it just needs to return a
    # number between 0 and the number of arms in the environment
    def chooseArm(self):
        pass

    #Processes a reward
    def processReward(self, arm, reward):
        pass


# Implements the epsilon-greedy algorithm as discussed in class
class EpsilonGreedy(MABLearner):

    def __init__(self, epsilon):
        #YOUR CODE HERE
        pass #remove once implemented
        
    def initWithEnvironment(self,env):
        #YOUR CODE HERE
        return False #Change to return True once implemented

    def chooseArm(self):
        #YOUR CODE HERE
        pass #remove once implemented

    def processReward(self,arm, reward):
        #YOUR CODE HERE
        pass #remove once implemented

# Implements the UCB algorithm as discussed in class
class UCB(MABLearner):

    def __init__(self, alpha):
        #YOUR CODE HERE
        pass #remove once implemented
        
    def initWithEnvironment(self,env):
        #YOUR CODE HERE
        return False #Change to return True once implemented

    def chooseArm(self):
        #YOUR CODE HERE
        pass #remove once implemented
        
    def processReward(self,arm, reward):
        #YOUR CODE HERE
        pass #remove once implemented

# Implements the Beta-Bernoulli thompson sampling algorithm as discussed
#in class.
#Should handle the straightforward extension to non-discrete variables.
class ThompsonDiscrete(MABLearner):

    def __init__(self):
        pass #remove once implemented
        
    def initWithEnvironment(self,env):
        #YOUR CODE HERE
        return False #Change to return True once implemented

    def chooseArm(self):
        #YOUR CODE HERE
        pass #remove once implemented
        
    def processReward(self,arm, reward):
        #YOUR CODE HERE
        pass #remove once implemented




        

