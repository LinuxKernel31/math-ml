__author__ = 'Robert Navas, Flomer Aduna'



m_array1= [[2,1,3],[1,3,6],[1,4,7]]
m_array2= [[1,4,3],[1,7,1],[1,6,3]]

result_matrix = [[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(m_array1)):
    for j in range(len(m_array1[0])):
        for k in range(len(m_array2[0])):
            result_matrix[i][j] += m_array1[i][k] * m_array2[k][j]


print(result_matrix)