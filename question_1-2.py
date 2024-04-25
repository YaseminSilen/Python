# Will be tested only with number an integer.
#
# If number is positive, returns a positive integer.
# If number is negative, returns a negative integer.
#
# The digits of the returned integer are the digits of number
# ordered from largest to smallest.

def reorder(number):
    '''
    >>> reorder(0)
    0
    >>> reorder(2)
    2
    >>> reorder(-33)
    -33
    >>> reorder(202)
    220
    >>> reorder(242242)
    442222
    >>> reorder(-3210123)
    -3322110
    >>> reorder(22659717106393887106)
    99887776665332211100
    '''

    if number < 0:
        string = str(number)[1:]
        sort = sorted(string, reverse=True)
        string = ''.join(sort)
        return -int(string)
    else:
        string = str(number)
        sort = sorted(string, reverse=True)
        string = ''.join(sort)
        return int(string)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
