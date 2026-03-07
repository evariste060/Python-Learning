matrix = [[1,1,1],[1,0,1],[1,1,1]]
zero_row = set()
zero_col = set()
col = len(matrix[0])
for i in range(len(matrix)):
    for j in range(col):
        if matrix[i][j] == 0:
            zero_row.add(i)
            zero_col.add(j)
for r in zero_row:
    for i in range(col):
        matrix[r][i] = 0
for c in zero_col:
    for i in range(len(matrix)):
        matrix[i][c] = 0