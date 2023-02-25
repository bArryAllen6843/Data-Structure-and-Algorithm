class Solution():
    def rotate(self, matrix):
        for row in matrix:
            row.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        return matrix


if __name__ == '__main__':
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    A = Solution()
    print(A.rotate(m))