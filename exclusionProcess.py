import random;
import math;
import statistics;
import matplotlib;
import matplotlib.pyplot as plt;
import numpy as np;

# Value for the invariant Bernoulli measure
alpha = 0.5
# The size of the integer lattice
N = 100
# The amount of time we run each sample
T = 100

# Evolves the state of the particles according to the exclusion rule
def iterate(states):
    newStates = states
    x = random.choice(list(states))
    rand = random.choice([0,1])
    if rand == 0 and ((x+1)%N) not in newStates:
        newStates.remove(x)
        newStates.add((x+1)%N)
    elif rand == 1 and ((x-1)%N) not in newStates:
        newStates.remove(x)
        newStates.add((x-1)%N)
    return newStates

# A mean 0 cylinder function
def V(states):
    if 0 in states:
        return 0.5
    else:
        return -0.5

def sample():
    states = set({})
    numberOfParticles = 0
    sum = 0
    t=0

    #Samples the Bernoulli(alpha) distribution
    for x in range(0,N):
        rand  = random.choices([0,1],weights=[alpha,1-alpha])
        if rand == [0]:
            states.add(x)
            numberOfParticles += 1

    #Each particle has an exponential clock at rate 1 independent of one another
    while(t<T):
        step = np.random.exponential(scale = 1/numberOfParticles)
        sum = sum + V(states)*step
        states = iterate(states)
        t=t+step

    return(sum/math.sqrt(t))


def simulate(n):
    samples = []
    for x in range(0,n):
        samples.append(sample())

    plt.hist(samples, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Frequency') 
    plt.show()
    
    return [statistics.mean(samples),statistics.variance(samples)]

print(simulate(10000))


