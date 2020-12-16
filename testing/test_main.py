import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_blockVals(self) :
        for bb in block_sizes : 
            nblocks = int( len( eng ) / bb ) 
            myblocks, myaverage, mysq = nblocks*[0], 0, 0
            for i in range(nblocks) :
                myblocks[i] = sum( eng[i*bb:(i+1)*bb] ) / bb 
                myaverage = myaverage + myblocks[i] 
                mysq = mysq + myblocks[i]*myblocks[i]
  
            mysq, myaverage = mysq / nblocks, myaverage / nblocks
            myvar = ( nblocks / (nblocks - 1) )*( mysq - myaverage*myaverage )
            myerr = np.sqrt( myvar / nblocks )
            self.assertTrue( np.abs( myerr - block_average( bb, eng ) ) < 1e-7, "Your function does not do block averaging correctly" )
