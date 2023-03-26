from math import factorial


class Solution:
    def uniquePaths(self, m, n):
        # def dfs(i, j):
        #     if i >= m or j >= n: return 0
        #     if i == m - 1 and j == n - 1: return 1
        #     return dfs(i + 1, j) + dfs(i, j + 1)
        #
        # return dfs(0, 0)

        return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)

if __name__ == '__main__':
    m = 3
    n = 2
    a = Solution()
    print(a.uniquePaths(m, n))
