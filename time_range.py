import numpy as np
from datetime import datetime, timedelta

def create_range(t1, t2, steps):
    rng = t2 - t1
    dt = rng / steps
    return np.array([t1 + dt*i for i in range(steps+1)])
  
