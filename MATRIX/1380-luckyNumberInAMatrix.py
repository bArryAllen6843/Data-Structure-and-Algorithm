class Solution:
    def luckyNumbers(self, matrix):
        # mi = [min(row) for row in matrix]
        # ma = [max(col) for col in zip(*matrix)]
        #
        # return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == ma[j]]

        # OR

        minrow = {min(r) for r in matrix}
        maxcol = {max(c) for c in zip(*matrix)}
        return list(minrow & maxcol)


if __name__ == '__main__':
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    A = Solution()
    print(A.luckyNumbers(matrix))
