def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n): matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n): matrix[i].reverse()

if __name__ == "__main__":
    m = [[1, 2], [3, 4]]; rotate_matrix(m); print(m)
