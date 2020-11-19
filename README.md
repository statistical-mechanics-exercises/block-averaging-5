# The relationship between the error and the size of the blocks

In this final exercise we are going to bring together everything we have learned in order to look at how the block averaging technique allows us to resolve the problems that we would otherwise have in estimating errors with correlated variables.

The previous four exercises have shown you how to compute the average and the standard deviation by block averaging.   In this exercise we are going to look at how the size of the error depends on the size of the blocks.  To do this we will need to encapsulate the code that we have written to calculate block averages and errors in a function that takes as input the data and the length of the block, M, into which to divide the data.  In `main.py` I have written the first line of this function for you as follows

````
def block_average( M, data ) :
    # Your code goes here

    return error
````

You will see that I have also called this function multiple times with different block sizes and made a list containing the size of the error for each of these block sizes.  I have then plotted a graph showing the size of the error against the block size.

Use what you have learnt in the exercise to complete the function and look at the graph produced.  

You should see that error is initially small.  It will then grow as the size of the various blocks is increased before plateauing to a constant value. 
