try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

myeng = np.loadtxt("energies")[:,1]

class UnitTests(unittest.TestCase) :
    def test_blockVals(self) :
        inputs, outputs = [], []
        for bb in [10,20,30,40,60,100,120,200,300,400] : 
            inputs.append((bb,myeng,))
            nblocks = int( len( eng ) / bb ) 
            myaverage, mysq = 0, 0
            for i in range(nblocks) :
                myblocks = sum( myeng[i*bb:(i+1)*bb] ) / bb 
                myaverage = myaverage + myblocks 
                mysq = mysq + myblocks*myblocks
  
            mysq, myaverage = mysq / nblocks, myaverage / nblocks
            myvar = ( nblocks / (nblocks - 1) )*( mysq - myaverage*myaverage )
            outputs.append( np.sqrt( myvar / nblocks ) )
        assert( check_func('block_average',inputs, variables ) )
