import collections


class Solution:
    def minReorder(self, n: int, connections) -> int:
        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)
        # appending bi directional connections in the graph
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)
        # checking if a city u is connected to parent also its reverse is present in set roads
        # it means we have to change the direction of that road that's why we are incrementing in res
        # if a city u has a parent v that matches the current parent then that road is in correct direction so do
        # nothing otherwise make v as city u and u as a parent city and check for the same
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)

        dfs(0, -1)
        return self.res


if __name__ == '__main__':
    # n = 6
    # connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    a = Solution()
    print(a.minReorder(n, connections))
