import random
position =0
walk = [position]
steps = 1000

for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

#creates a walking route




import numpy as np
nsteps = 1000
draws = np.random.randint(0,2, size=nsteps)
steps = np.where(draws>0,1,-1)
walk = steps.cumsum()
walk.min()
walk.max()

(np.abs(walk)>=10).argmax() #gives the position where ten-step is reached
#as walk is either a step forward or backward, this gives the final count


nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2,size = (nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0,1,-1)
walks = steps.cumsum(1)
#this calculates for 5000 walks
# print(walks)
# print(walks.max())
# print(walks.min())

hits30 = (np.abs(walks)>= 30).any(1) #which walks crossed 30, boolean
hits30.sum() # number of trues

crossing_times = (np.abs(walks[hits30])>=30).argmax(1)
crossing_times.mean()
