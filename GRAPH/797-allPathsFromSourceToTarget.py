class Solution:
    def allPathsSourceToTarget(self, graph):
        n = len(graph)
        ans = []
        currentPath = [0]

        def paths():
            # if target equal to last element in currentPath then we found a path so add in ans
            if n - 1 == currentPath[-1]:
                ans.append(currentPath[:])
            for el in graph[currentPath[-1]]:
                currentPath.append(el)
                paths()
                currentPath.pop()

        paths()
        return ans


if __name__ == '__main__':
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    a = Solution()
    print(a.allPathsSourceToTarget(graph))
