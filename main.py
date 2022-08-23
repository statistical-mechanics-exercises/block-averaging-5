import matplotlib.pyplot as plt
import numpy as np

def block_average( M, data ) :
  # Your code goes here
  nblocks = int( np.floor(len(data) / M) ) 
  blocks = nblocks*[0]

  k=0
  for i in range( len(eng) ) :
    blocks[k] = blocks[k] + eng[i] 
    if (i+1)%M==0 and i>0 : 
      blocks[k] = blocks[k] / M
      k = k + 1
  
  mean, sq = 0, 0  
  for bb in blocks : mean, sq = mean + bb, sq + bb*bb
  average, sq = mean / len(blocks), sq / len(blocks)
  var = ( len(blocks) / ( len(blocks) - 1 ) ) * ( sq - average*average )
  error = np.sqrt( var / len(blocks) ) 
  return error

# Read in the energies from a file
eng = np.loadtxt("energies")[:,1]

