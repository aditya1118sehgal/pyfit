import numpy as np
from common import getArgs

def getLinearFit (coords):
    x = np.array (coords[0])
    y = np.array (coords[1])
    m, b = np.polyfit (x, y, 1)
    print 'y = {m} * x + {b}'.format (m = m, b = b)

coords = getArgs ()
getLinearFit (coords)
