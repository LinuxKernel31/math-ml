from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__  = 'Robert Navas'

def transpose():
    sample_matrix = [[1,2],[3,4],[5,6]]

    result_matrix = [[0,0,0], [0,0,0]]

    for i in range(len(sample_matrix)):
        for j in range(len(sample_matrix[0])):
            result_matrix[j][i] = sample_matrix[i][j]

    return result_matrix

if __name__ == '__main__':

    print(transpose())

