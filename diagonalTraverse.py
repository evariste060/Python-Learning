def findDiagonalOrder(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for d in range(rows + cols - 1):
        temp = []
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                temp.append(mat[i][j])
        if d % 2 == 0:
            temp.reverse()
        result.extend(temp)
    return result