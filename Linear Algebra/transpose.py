from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__  = 'Robert Navas'

def transpose_fixed():
    sample_matrix = [[1,2],[3,4],[5,6]]

    result_matrix = [[0,0,0], [0,0,0]]

    for i in range(len(sample_matrix)):
        for j in range(len(sample_matrix[0])):
            result_matrix[j][i] = sample_matrix[i][j]

    return result_matrix

def transpose(rows, cols):

    result_matrix = []
    final_matrix = []
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(0)

        final_matrix.append(temp)

    for row in range(rows):
        row_appender = []
        for col in range(cols):
            row_appender.append(int(input("[{},{}] value: ".format(row,col))))

        result_matrix.append(row_appender)

    print("Matrix Before Transpose: ", result_matrix)

    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[0])):
            final_matrix[j][i] = result_matrix[i][j]

    return final_matrix

def matrix_input():

    rows = int(input("Input number of rows: "))
    cols = int(input("Input number of columns: "))

    result_matrix = []

    for row in range(rows):
        row_appender = []
        for col in range(cols):
            row_appender.append(int(input("[ {}, {} ] value: ".format(row, col))))

        result_matrix.append(row_appender)


    return result_matrix




if __name__ == '__main__':

    print("Matrix After Tranpose: ", transpose(2,3))

