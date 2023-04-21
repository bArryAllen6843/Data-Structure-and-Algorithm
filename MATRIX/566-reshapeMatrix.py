class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        flatten = []
        reshape = []
        for row in mat:
            for num in row:
                flatten.append(num)

        if r * c != len(flatten):
            return mat
        else:
            for row_index in range(r):
                reshape.append(flatten[row_index * c: row_index * c + c])
            return reshape


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    a = Solution()
    print(a.matrixReshape(mat, r, c))
