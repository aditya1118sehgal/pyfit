import numpy as np
import sys

from common import getArgs, printInvalidCoord

def getLogFit (xy):

    x_data = np.array (xy[0])
    y_data = np.array (xy[1])

    log_x_data = np.log (x_data)
    log_y_data = np.log (y_data)

    curve = np.polyfit(log_x_data, y_data, 1)

    a = str(curve[0])
    b = str (abs (curve [1]))
    plusminus = ('-' if curve [1] < 0 else '+')

    print 'y = {a} * Math.log10 (x) {plusminus} {b}'.format (a = a, b = b, plusminus = plusminus)


coords = getArgs()
getLogFit (coords)
