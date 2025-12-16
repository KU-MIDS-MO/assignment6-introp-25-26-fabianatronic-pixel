import numpy as np
def estimate_pi(num_samples):   #number of random points to generate
    inside_circle = 0             # it's a counter, it counts  how many points fall inside the circle
                                 #It starts from 0 because no points have been checked yet.
    for i in range (num_samples):    #repeat the instructions below "num_samples" times
        x, y = np.random.rand(2)   # generates TWO RANDOM NUMBERS IN [0,1)
                                   #x and y are the coordinates of a point
                                   #It is like choosing a random point inside a 1×1 square.
        if x**2 + y**2 <= 1:          #Here we check if the point is inside the circle.
            inside_circle += 1     #If the point is inside the circle:
                                   #I increase the counter by 1, I am counting the “good” points.
            
    pi_estimate = 4* inside_circle / num_samples   #4*proportion of points inside the circle
    return pi_estimate
    
#♦The function estimates π by generating random points in a square and counting how many fall inside a quarter of a circle. 
#%%
#Write a function:
#`estimate_pi(num_samples)`
#that:
#returns an estimate of π using num_samples random points generated with np.random.rand().