def set_zeroes(matrix):
    r, c = len(matrix), len(matrix[0])
    row_zero = col_zero = False
    for i in range(r):
        if matrix[i][0] == 0: col_zero = True
    for j in range(c):
        if matrix[0][j] == 0: row_zero = True
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][j] == 0: matrix[i][0] = 0; matrix[0][j] = 0
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
    if row_zero:
        for j in range(c): matrix[0][j] = 0
    if col_zero:
        for i in range(r): matrix[i][0] = 0

if __name__ == "__main__":
    m = [[1, 0], [1, 1]]; set_zeroes(m); print(m)
