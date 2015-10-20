"""
Merge function for 2048 game.
http://codeskulptor-user40.commondatastorage.googleapis.com/user40_FimKdOQdX2_3.py
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    tmp = filter(None,line)
    
    for cnt in range(len(tmp)-1):
        if tmp[cnt] == tmp[cnt+1]:
            tmp[cnt]=2*tmp[cnt]
            tmp[cnt+1]=0

    result = filter(None,tmp)
    result = result + [0]*(len(line)-len(result))
    return result
