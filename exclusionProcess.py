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

# Evolves the state of the particles according to the exclusion rule
def iterate(states,particleStates):
    
    particleIndex = random.randint(0,len(particleStates)-1)
    j = particleStates[particleIndex]
    rand = bool(random.getrandbits(1))
    
    if rand and states[(j+1)%N] == False:
        states[j] = False
        states[(j+1)%N] = True
        particleStates[particleIndex] = (j+1)%N
    elif rand and states[(j-1)%N] == False:
        states[j] = False
        states[(j-1)%N] = True
        particleStates[particleIndex] = (j-1)%N

# A mean 0 cylinder function
def V(states):
    if states[0]== False:
        return 0.5
    else:
        return -0.5

def sample(T):
    states = []
    particleStates = []
    
    #Samples the Bernoulli(alpha) distribution
    for x in range(0,N):
        rand = bool(random.getrandbits(1))
        states.append(rand)
        if rand == True:
            particleStates.append(x)
    
    numberOfParticles = len(particleStates)
    sum = 0
    t=0

    #Each particle has an exponential clock at rate 1 independent of one another
    while(t<T):
        step = np.random.exponential(scale = 1/numberOfParticles)
        sum = sum + V(states)*step
        iterate(states,particleStates)
        t=t+step
    return(sum/math.sqrt(t))


def simulate(n,T):
    samples = []
    
    for x in range(0,n):
        samples.append(sample(T))

    plt.hist(samples, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Frequency') 
    plt.show()

    m = statistics.mean(samples)
    
    return [statistics.mean(samples),statistics.variance(samples,m)]

simulate(10000,100)