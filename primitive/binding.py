
'''
Provides the basic spells for binding two items together and
subsequently extracting them.
'''

###############################################################################

def pair(x, y):
    '''
    Returns a single item containing both x and y.
    '''

    return (x, y)

##################################################

def is_atomic(x):
    '''
    Returns True if x is not a pair. Otherwise returns False.
    '''

    return not is_pair(x)

##################################################

def is_pair(x):
    '''
    Returns True if the given x is a pair. Otherwise returns False.
    '''

    try:
        assert(len(x) is 2)
    except:
        return False
    else:
        return True

##################################################

def left(pair):
    '''
    Returns the first element of a pair.

    >>> left(pair(1, 2))
    1
    >>> left(pair(3, 4))
    3
    '''

    return pair[0]

##################################################

def right(pair):
    '''
    Returns the second element of a pair.

    >>> right(pair(1, 2))
    2
    >>> right(pair(3, 4))
    4
    '''

    return pair[1]

