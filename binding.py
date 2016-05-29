
from primitive.binding import pair, left, right, is_pair, is_atomic

###############################################################################

def make_list(*args):
    pass

##################################################

def is_list(x):
    '''
    Returns True if the given x is the result of make_list. Otherwise
    returns False.
    '''

    pass

##################################################

def equal(list1, list2):
    '''
    Returns True if the given lists each have identical elements. Otherwise
    returns false.
    '''

    pass

##################################################

def list_to_string(list):
    '''
    Returns a string representation of the given list.

    >>> list_to_string(make_list(1, 2, 3))
    '(1, 2, 3)'
    >>> list_to_string(make_list(1, make_list(101, 102), 2, 3))
    '(1, (101, 102), 2, 3)'
    '''

    pass

##################################################

def length(list):
    '''
    Returns the length of the given list.

    >>> length(make_list(1, 2, 3))
    3
    >>> length(make_list())
    0
    '''

    pass


##################################################

def index(list, n):
    '''
    Returns the nth element of the given list.
    '''

    pass

##################################################

def append(list, value):
    '''
    Returns a new list which matches the given list except that it has
    the given value appended.

    >>> append(make_list(1, 2), 3)
    (1, 2, 3)
    '''

    pass

##################################################

def insert(list, index, value):
    '''
    Returns a new list which matches the given list except that it has
    the given value inserted at the given index.

    >>> insert(make_list(1, 3), 1, 2)
    (1, 2, 3)
    '''

    pass

##################################################

def replace(list, index, value):
    '''
    Returns a new list which matches the given list except that the value
    at the given index is set to the given value.

    >>> replace(make_list(1, 3), 1, 2)
    (1, 2)
    '''

    pass

##################################################

def zip(list1, list2):
    '''
    Takes two lists and returns a single list of the combined values. If
    the lists are of different lengths, then extra values from the longer
    list are ignored.

    >>> zip(make_list(1, 2, 3), make_list(4, 5, 6))
    ((1, 4), (2, 5), (3, 6))
    >>> zip(make_list(1, 2, 3), make_list(4, 5))
    ((1, 4), (2, 5))
    '''
    
    pass

##################################################

def zip_longest(list1, list2, default=None):
    '''
    Takes two lists and returns a single list of the combined values. If
    the lists are of different lengths, then extra values from the longer
    list are combined with the default value.

    >>> zip_longest(make_list(1, 2, 3), make_list(4, 5, 6))
    ((1, 4), (2, 5), (3, 6))
    >>> zip_longest(make_list(1, 2, 3), make_list(4, 5))
    ((1, 4), (2, 5), (3, None))
    >>> zip_longest(make_list(1, 2), make_list(3, 4, 5))
    ((1, 3), (2, 4), (None, 5))
    '''
    
    pass

##################################################

def filter(f, list):
    '''
    Returns a new list containing only elements from the given list
    that cause f to return True.

    >>> equal(filter(even, make_list(1, 2, 3, 4)), make_list(2, 4))
    True
    '''

    pass

##################################################

def map(f, list):
    '''
    Returns a new list with f applied to every element from the given list.
    f should therefore be a callable that takes one argument.

    >>> equal(map(square, make_list(2, 10)), make_list(4, 100))
    True
    >>> equal(map(absolute, make_list(-2, 2)), make_list(2, 2))
    True
    >>> equal(map(absolute, make_list(-2, 2)), make_list(-2, 2))
    False
    '''

    pass

##################################################

def reduce(f, list, initial=None):
    '''
    Applies f to each element in the list, where f is a callable with two
    arguments. The first argument is the value last returned by f, the second
    argument is the element in the list. Returns the last value given by f.

    When applying f to the first element in the list, the first argument is
    the given initial value.

    >>> reduce(sum, make_list(1, 2, 3), 0)
    6
    >>> reduce(lambda x, y: x and even(y), make_list(1, 2, 3))
    False
    >>> reduce(lambda x, y: x and even(y), make_list(2, 4, 6))
    True
    '''

    pass

