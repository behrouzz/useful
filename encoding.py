"""
Modul bstools - (to be completed)
=============
"""

import base64, pickle
import matplotlib.pyplot as plt

def obj2str(obj):
    """
    Convert python object to base64 string

    Parameters
    ----------
        obj : python object

    Returns
    -------
        string
    """
    serialized = pickle.dumps(obj)
    b64byte = base64.encodebytes(serialized)
    return b64byte.decode('utf-8')

def str2obj(string):
    """
    Convert base64 string to python object

    Parameters
    ----------
        string : string

    Returns
    -------
        python object
    """
    b64byte = string.encode('utf-8')
    serialized = base64.decodebytes(b64byte)
    return pickle.loads(serialized)

# Convert python object to string
# -------------------------------

obj = plt.imread('data/bs.jpg')

string = obj2str(obj)

with open('data/bs_string.txt', 'w') as f:
    f.write(string)

# Convert string to python object
# -------------------------------

with open('data/bs_string.txt', 'r') as f:
    string = f.read()

obj = str2obj(string)

plt.imshow(obj)
plt.show()
