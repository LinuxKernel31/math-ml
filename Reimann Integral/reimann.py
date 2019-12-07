from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

__author__  = 'Robert Navas'
__version__ = '1.0.0'


def delta_x(upper_limit, lower_limit, n):

    return (upper_limit - lower_limit) / n

def get_values(upper_limit, lower_limit, n):

    values = []
    ranges = 0 
    values.append(lower_limit)

    for _ in range(n):

        ranges += delta_x(upper_limit, lower_limit, n)

        if ranges == upper_limit:
            break
        else:
            values.append(ranges)

    return values






    