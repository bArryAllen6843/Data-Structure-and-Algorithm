class Solution:
    def countNegatives(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        negative = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    negative += 1
        return negative


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    a = Solution()
    print(a.countNegatives(grid))
