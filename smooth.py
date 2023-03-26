import numpy as np

def smooth(arr, offset):
    # width (length) of window:
    width = 2*offset + 1
    new_arr = np.ones(arr.size - width + 1)
    for i,val in enumerate(new_arr):
        new_arr[i] = np.mean(arr[i:i+width])
    return new_arr
