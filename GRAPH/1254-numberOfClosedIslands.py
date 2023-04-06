class Solution(object):
    def closedIsland(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j, val):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = val
                dfs(i, j + 1, val)
                dfs(i + 1, j, val)
                dfs(i - 1, j, val)
                dfs(i, j - 1, val)

        for i in range(m):
            for j in range(n):
                # this condition makes boundary zeroes to 1 which can never be closed islands
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j, 1)

        res = 0
        # left all zeroes are closed islands so whenever this loop finds a zero it will convert all
        # connected zeroes to 1 which states that it is an island so increment count of res
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
        return res


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    a = Solution()
    print(a.closedIsland(grid))
