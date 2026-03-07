matrix  = [[1,1,1],[1,0,1],[1,1,1]]
for row_i in range(len(matrix)):
    for col_i in range(len(matrix[row_i])):
        if matrix[row_i][col_i]== 0:
            print(matrix[row_i])