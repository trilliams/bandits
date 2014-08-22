bandits
=======

Growing collection of algorithms for multi-armed bandit modeling. After loading bandits.py, call bandit() with a variable number of rounds to see the algorithm in action. Each action is a normal random variable with mean and standard deviation chosen as uniform random variables in the ranges defined by [lb_mu,ub_mu] and [lb_sigma,ub,sigma], respectively. Variance is, of course, the standard deviation squared. The bandit will then simulate for the given number of rounds, each time showing the chosen action, reward from that, and the total reward in general. Decisions are made according to the UCB1 algorithm, a great description of which is linked to below.

Soon to come:  
-more solution algorithms   
-more options for reward distributions   
-graphical comparisons of algorithms   

UCB1:
http://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/

Example run (excluding final output):
>>> bandit(30,10)
1: action 1 gives -13.24, total reward: -13.24
2: action 2 gives 38.38, total reward: 25.15
3: action 3 gives 35.76, total reward: 60.91
4: action 4 gives 13.23, total reward: 74.14
5: action 5 gives 12.50, total reward: 86.65
6: action 6 gives 2.24, total reward: 88.89
7: action 7 gives 28.47, total reward: 117.35
8: action 8 gives 44.57, total reward: 161.93
9: action 9 gives 7.04, total reward: 168.97
10: action 10 gives 14.43, total reward: 183.40
11: action 8 gives 42.67, total reward: 183.40
12: action 8 gives 42.55, total reward: 183.40
13: action 8 gives 42.56, total reward: 183.40
14: action 8 gives 39.82, total reward: 183.40
15: action 8 gives 42.24, total reward: 183.40
16: action 8 gives 41.72, total reward: 183.40
17: action 8 gives 41.87, total reward: 183.40
18: action 8 gives 41.28, total reward: 183.40
19: action 8 gives 45.27, total reward: 183.40
20: action 8 gives 42.72, total reward: 183.40
21: action 8 gives 41.66, total reward: 183.40
22: action 8 gives 40.65, total reward: 183.40
23: action 8 gives 42.06, total reward: 183.40
24: action 8 gives 42.85, total reward: 183.40
25: action 8 gives 40.43, total reward: 183.40
26: action 8 gives 39.19, total reward: 183.40
27: action 8 gives 43.10, total reward: 183.40
28: action 8 gives 43.14, total reward: 183.40
29: action 8 gives 41.71, total reward: 183.40
30: action 8 gives 41.01, total reward: 183.40

Action 1 had mean 11.10 and variance 16.16
Action 2 had mean 38.60 and variance 5.08
Action 3 had mean 37.31 and variance 2.46
Action 4 had mean 13.48 and variance 9.08
Action 5 had mean 13.50 and variance 0.95
Action 6 had mean 3.02 and variance 5.61
Action 7 had mean 0.00 and variance 9.13
Action 8 had mean 41.20 and variance 1.83
Action 9 had mean 3.41 and variance 5.37
Action 10 had mean 31.73 and variance 16.82

The best action was 8, with mean 41.20.
Your total reward is 183.40.
Your cumulative regret is thus 1052.64
