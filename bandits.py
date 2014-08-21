import numpy as np

def bandit(num_rounds,num_actions,lb_mu=0,ub_mu=50,lb_sigma=0,ub_sigma=5):
    #Simulates a multi-armed bandit via UCB1 using n actions over T rounds
    totals = []
    counts = []
    n = num_actions
    T = num_rounds
    #Determine the parameters of each action
    mus = list(np.random.uniform(lb_mu,ub_mu,n))
    sigmas = [np.random.uniform(lb_sigma,ub_sigma)**2 for i in range(n)]
    totalreward = 0
    for i in range(n):
        #Establish a baseline reward for each action 
        reward = np.random.normal(mus[i],sigmas[i])
        totals.append(reward)
        counts.append(1)
        totalreward += reward
        print "%i: action %i gives %.2f, total reward: %.2f" % \
              (i+1,i+1,reward,totalreward)
    estimates = ucb1estimatefinder(totals,counts,i+1)
    for i in range(n,T):
        #Now, choose an action based off of UBC1 estimates:
        choice = estimates.index(max(estimates))
        #Play best action
        reward = np.random.normal(mus[choice],sigmas[choice])
        totals[choice] += reward
        counts[choice] += 1
        print "%i: action %i gives %.2f, total reward: %.2f" % \
              (i+1,choice+1,reward,totalreward)
        estimates = ucb1estimatefinder(totals,counts,i+1)
    #Reveal parameters
    print ""
    for i in range(n):
        print "Action %i had mean %.2f and variance %.2f" % \
              (i+1,mus[i],sigmas[i])
    print ""
    #recap the situation, compute regret
    regret = max(mus)*T - totalreward
    print 'The best action was %i, with mean %.2f.' % \
          (mus.index(max(mus))+1,max(mus))
    print 'Your total reward is %.2f.' % totalreward
    print 'Your cumulative regret is thus %.2f' % regret
    return regret

def ucb1estimatefinder(totals,counts,t):
    #Implementation of the UCB1 update process
    estimates = [(totals[i]/counts[i] + np.sqrt((2*np.log(t)/counts[i]))) \
                 for i in range(len(totals))]
    return estimates
