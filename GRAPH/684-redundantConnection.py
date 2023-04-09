class Solution:
    def findRedundantConnection(self,edges):
        par = [x for x in range(1001)]
        for edge in edges:
            par_a, par_b = edge
            while par_a != par[par_a]:
                par_a = par[par_a]

            while par_b != par[par_b]:
                par_b = par[par_b]

            if par_a != par_b:
                par[par_a] = par_b
            else:
                return edge


if __name__ == '__main__':
    a = Solution()
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(a.findRedundantConnection(edges))
