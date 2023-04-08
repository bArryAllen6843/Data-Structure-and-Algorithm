class Solution:
    # replace all the ones which are at boundary with 0 then we will be left 1's which are surrounded by 0's from all
    # sides. We can simply count no of 1's which is the answer
    def numEnclaves(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 1:
                    dfs(i, j)
        return sum(sum(row) for row in grid)


if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    a = Solution()
    print(a.numEnclaves(grid))
