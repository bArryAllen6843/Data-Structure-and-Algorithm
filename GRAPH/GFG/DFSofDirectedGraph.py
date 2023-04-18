import collections


class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        vis = set()
        ans = []
        graph = self.addEdge(adj, V)
        for i in range(V):
            if i not in vis:
                self.dfs(i, graph, vis, ans)
        return ans

    # Recursive DFS function
    def dfs(self, node, graph, vis, ans):
        vis.add(node)
        ans.append(node)
        for neighbor in graph[node]:
            if neighbor not in vis:
                self.dfs(neighbor, graph, vis, ans)

    # Helper function to construct adjacency list
    def addEdge(self, adj, V):
        graph = collections.defaultdict(list)
        for vertex in range(V):
            for adjel in adj[vertex]:
                graph[vertex].append(adjel)
        return graph


if __name__ == '__main__':
    V = 5
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    a = Solution()
    print(a.dfsOfGraph(V, adj))
    # print(addEdge(adj,V))
