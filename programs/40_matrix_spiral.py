# Spiral order traversal of a matrix
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order(matrix))  # [1,2,3,6,9,8,7,4,5]
