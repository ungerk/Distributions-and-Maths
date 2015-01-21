"""Generate a bernoulli distribition based on the value of p."""

import random
import matplotlib.pyplot as plt

# Set the values of p and q
p = .75
q = 1 - p

# Define bernoulli function that assigns random numbers to variable r based on the value of p
def bernoulli(p):
	r = random.random()
	if r <= p:
		num = 1
	else:
		num = 0
	return num

# Generate a list to populate with values from bernoulli function
list = []

# Loop through bernoulli function 100 times and append each result to list
for i in range(0,100):
	list.append(bernoulli(p))

# Print average of all values in list
print 1.0*sum(list)/len(list)

# Generate a histogram that plots each value in list
plt.figure()
plt.hist(list, bins=2)
plt.ylim(-1,2)
plt.show()

		
