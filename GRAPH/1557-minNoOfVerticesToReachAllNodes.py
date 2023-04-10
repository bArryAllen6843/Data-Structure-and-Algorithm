class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        indegree = [0] * n
        # x is the source and y is the destination and indegree is for destination i.e. y here
        for x, y in edges:
            indegree[y] += 1

        ans = []
        # use in degree array to get the nodes with zero indegree
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        return ans


if __name__ == '__main__':
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    a = Solution()
    print(a.findSmallestSetOfVertices(n, edges))
