import sys

def getArgs ():
    numArgs = len(sys.argv)
    if numArgs < 4:
        print 'insufficient args'
        return
    else:
        coords = sys.argv[1:]
        x = []
        y = []
        for coord in coords:
            if coord.count(',') != 1:
                printInvalidCoord (coord)
                return
            else:
                xy = coord.split (',')
                try:
                    xcoord = float (xy[0])
                    ycoord = float (xy[1])
                except:
                    printInvalidCoord (coord)
                    return
                x.append (xcoord)
                y.append (ycoord)
        return x, y

def printInvalidCoord (coord):
    print 'invalid arg {coord}'.format (coord = coord)
