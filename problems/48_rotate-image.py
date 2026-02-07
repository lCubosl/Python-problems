class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

s = Solution()

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Input:")
print_matrix(matrix1)

s.rotate(matrix1)
print("Output:")
print_matrix(matrix1)
