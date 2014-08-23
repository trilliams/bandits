bandits
=======

Growing collection of algorithms for multi-armed bandit modeling. After loading bandits.py, call bandit() with a variable number of rounds to see the algorithm in action. Each action is a normal random variable with mean and standard deviation chosen as uniform random variables in the ranges defined by [lb_mu,ub_mu] and [lb_sigma,ub,sigma], respectively. Variance is, of course, the standard deviation squared. The bandit will then simulate for the given number of rounds, each time showing the chosen action, reward from that, and the total reward in general. Decisions are made according to the UCB1 algorithm, a great description of which is linked to below.

Soon to come:  
-more solution algorithms   
-more options for reward distributions   
-graphical comparisons of algorithms   

Dependencies:  
Numpy

UCB1:
http://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/

Example run (excluding final output):  
bandit(10,4)  
1: action 1 gives 49.58, total reward: 49.58  
2: action 2 gives 43.65, total reward: 93.23  
3: action 3 gives 35.07, total reward: 128.30  
4: action 4 gives 33.53, total reward: 161.83  
5: action 1 gives 33.18, total reward: 195.01    
6: action 2 gives 42.29, total reward: 237.31   
7: action 2 gives 33.45, total reward: 270.75  
8: action 1 gives 23.49, total reward: 294.25    
9: action 2 gives 39.87, total reward: 334.12    
10: action 2 gives 31.20, total reward: 365.31  
  
Action 1 had mean 22.53 and variance 13.25  
Action 2 had mean 33.88 and variance 3.69  
Action 3 had mean 47.53 and variance 16.40  
Action 4 had mean 33.87 and variance 1.12  
  
The best action was 3, with mean 47.53.  
Your total reward is 365.31.  
Your cumulative regret is thus 109.98.  
