import collections


class Solution:
    # if adj is given in this form => adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    # def bfsOfGraph(self, V: int, adj):
    #     vis = set()
    #     ans = []
    #     graph = self.addEdge(adj, V)
    #     for i in range(V):
    #         if i in vis:
    #             continue
    #
    #         vis.add(i)
    #         q = collections.deque([i])
    #         while q:
    #             el = q.popleft()
    #             ans.append(el)
    #             for nbr in graph[el]:
    #                 if nbr not in vis:
    #                     vis.add(nbr)
    #                     q.append(nbr)
    #     return ans
    #
    # def addEdge(self, adj, V):
    #     graph = collections.defaultdict(list)
    #     for vertex in range(V):
    #         for adjel in adj[vertex]:
    #             graph[vertex].append(adjel)
    #     return graph

    def bfs(self, adj, V):
        adj = self.create_adj(adj, V)
        vis = set()
        ans = []
        i = 0
        while i == 0:
            if i in vis:
                continue
            vis.add(i)

            q = collections.deque([i])
            while q:
                el = q.pop()
                ans.append(el)

                for adjel in range(V):
                    if adj[el][adjel] and adjel not in vis:
                        vis.add(adjel)
                        q.appendleft(adjel)
            i += 1
        return ans

    # if the edges given are in the form of tuple then apply this func
    # def create_adj(self, edges, V):
    #     ad = [[0] * V for _ in range(V)]
    #
    #     for e in edges:
    #         ad[e[0]][e[1]] = ad[e[1]][e[0]] = 1
    #     return ad

    # if the edges given are in the form of list then apply this func
    def create_adj(self, edges, V):
        ad = [[0] * V for _ in range(V)]
        for e in edges:
            print(e)
            ad[e[0]][e[1]] = ad[e[1]][e[0]] = 1
        return ad

if __name__ == '__main__':
    # adj = [(0, 2), (0, 5), (1, 5), (1, 6), (1, 8), (3, 4), (3, 5), (4, 7), (5, 7)]
    # adj = [[0, 8], [1, 6], [1, 7], [1, 8], [5, 8], [6, 0], [7, 3], [7, 4], [8, 7], [2, 5]]
    # adj = [[0, 2], [0, 5], [1, 5], [1, 6], [1, 8], [3, 4], [3, 5], [4, 7], [5, 7]]
    adj = [[0, 1]]
    V = 2
    a = Solution()
    print(a.bfs(adj, V))
