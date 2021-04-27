def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

def zigzag(matrix, n, m):
    size = n * m
    number = 1
    for i in range(n):
        if i % 2 is 0:
            print(str(i), ": double")
            for j in range(m):
                print("i:", str(i), "j:", str(j), "number:", str(number))
                matrix[i][j] = number
                number = number + 1
        else:
            print(str(i), ": odd")
            for j in range(m):
                print("i:", str(i), "j:", str(m - j - 1), "number:", str(number))
                matrix[i][m - j - 1] = number
                number = number + 1
def spiral(matrix):
    pass


matrix = [[0 for c in range(5)] for r in range(5)]
print_matrix(matrix, 5,5)
zigzag(matrix, 5, 5)
# print(matrix)
# matrix[0][4] = 100
print_matrix(matrix, 5,5)
