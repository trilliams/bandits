bandits
=======

Growing collection of algorithms for multi-armed bandit modeling. After loading bandits.py, call bandit() with a variable number of rounds to see the algorithm in action. Each action is a normal random variable with mean and standard deviation chosen as uniform random variables in the ranges defined by [lb_mu,ub_mu] and [lb_sigma,ub,sigma], respectively. Variance is, of course, the standard deviation squared. The bandit will then simulate for the given number of rounds, each time showing the chosen action, reward from that, and the total reward in general. Decisions are made according to the UCB1 algorithm, a great description of which is linked to below.

Soon to come:  
-more solution algorithms   
-more options for reward distributions   
-graphical comparisons of algorithms   

UCB1:
http://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/


