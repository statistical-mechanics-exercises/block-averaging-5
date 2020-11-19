import matplotlib.pyplot as plt
import numpy as np

def block_average( M, data ) :
  # Your code goes here
  
  return error

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

# Now calculate the block averages for different block sizes
# Now calculate the block averages for different block sizes
i, errors, block_sizes = 0, 10*[0], [10,20,30,40,60,100,120,200,300,400]
for bb in block_sizes :
  errors[i] = block_average( bb, eng )
  i = i + 1
  
# And plot a graph
plt.plot( block_sizes, errors, 'k.-' )
plt.savefig("myplot.png")

