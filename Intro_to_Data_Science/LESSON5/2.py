import numpy as np
from sklearn.metrics import r2_score

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    up_sum = (((data - predictions) ** 2)).sum()
    bottom_sum = ((data - np.mean(data)) ** 2).sum()
    r_squared = 1  - float((up_sum / float(bottom_sum)))
    #r_squared = r2_score(data,predictions)
    
    
    
    

    return r_squared