class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    a = Solution()
    print(a.isToeplitzMatrix(matrix))
