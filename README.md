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
1: action 1 gives 12.42, total reward: 12.42  
2: action 2 gives 30.47, total reward: 42.89  
3: action 3 gives 0.78, total reward: 43.67   
4: action 4 gives 45.73, total reward: 89.40    
5: action 5 gives 14.37, total reward: 103.77  
6: action 6 gives 27.93, total reward: 131.70  
7: action 7 gives 10.46, total reward: 142.16  
8: action 8 gives 6.75, total reward: 148.91  
9: action 9 gives -15.80, total reward: 133.11  
10: action 10 gives 2.95, total reward: 136.05  
11: action 4 gives 53.43, total reward: 189.49  
12: action 4 gives 29.69, total reward: 219.17  
13: action 4 gives 67.07, total reward: 286.24  
14: action 4 gives 71.23, total reward: 357.47  
15: action 4 gives 52.09, total reward: 409.56  
16: action 4 gives 35.63, total reward: 445.19  
17: action 4 gives 46.17, total reward: 491.36  
18: action 4 gives 39.62, total reward: 530.98  
19: action 4 gives 30.84, total reward: 561.82  
20: action 4 gives 43.60, total reward: 605.42  
21: action 4 gives 41.37, total reward: 646.79  
22: action 4 gives 38.57, total reward: 685.36  
23: action 4 gives 23.19, total reward: 708.55  
24: action 4 gives 40.18, total reward: 748.72  
25: action 4 gives 58.87, total reward: 807.60  
26: action 4 gives 42.55, total reward: 850.15  
27: action 4 gives 39.10, total reward: 889.25  
28: action 4 gives 58.83, total reward: 948.08  
29: action 4 gives 53.12, total reward: 1001.20  
30: action 4 gives 64.39, total reward: 1065.59  
  
Action 1 had mean 12.48 and variance 0.06  
Action 2 had mean 30.47 and variance 0.01  
Action 3 had mean 17.82 and variance 20.74  
Action 4 had mean 48.86 and variance 13.42  
Action 5 had mean 17.03 and variance 8.73  
Action 6 had mean 27.92 and variance 0.04  
Action 7 had mean 26.10 and variance 12.31  
Action 8 had mean 11.74 and variance 14.91  
Action 9 had mean 36.59 and variance 24.64  
Action 10 had mean 1.67 and variance 1.49  
  
The best action was 4, with mean 48.86.  
Your total reward is 1065.59.  
Your cumulative regret is thus 400.31   
