"""Generate an approximate calculation of pi using the ratio of pixels inside and outside of a circle. """ 

import random
import matplotlib.pyplot as plt

# Create lists to hold the various generated values of x and y
listx = []
listy = []

# Create status variables to keep track of the number of pixels inside and outside of the circle
countin = 0
countout = 0

# Generate 10000 random values for x and y
for i in range(0,10000):
	x = 2*random.random() - 1
	y = 2*random.random() - 1
	# print x, y
	
	if (x**2 + y**2) <= 1.0:  # Use the formula for a circle to define bounds of inner and outer pixels
		countin += 1
		listx.append(x) # Only generate values of x and y inside circle
		listy.append(y)
	else:
		countout += 1
		

# Calculate pi based on ratio of pixels inside circle to all pixels
print 4.0*countin/(countin + countout)

# Generate plot of each x,y coordinate
plt.figure(figsize=(5,5))
plt.plot(listx,listy, 'c.')
plt.show()
