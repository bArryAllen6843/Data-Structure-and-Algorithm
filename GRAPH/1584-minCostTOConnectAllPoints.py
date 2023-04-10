import heapq


class Solution:
    def solve(self, points):
        n = len(points)
        dist = []

        # every absolute distance is calculated and stored in min heap with their coordinates as i and j
        for i in range(n):
            for j in range(i + 1, n):
                dist.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        heapq.heapify(dist)

        # union find method implemented below
        # all distances are stored in heap and through union find if a distance is not redundant then its distance
        # value is added in min spanning tree
        parent = [x for x in range(n)]
        min_spanning_tree = 0
        while n > 1:
            d, i, j = heapq.heappop(dist)
            pari, parj = parent[i], parent[j]
            while parent[pari] != pari:
                pari = parent[pari]
            while parent[parj] != parj:
                parj = parent[parj]

            if pari != parj:
                n -= 1
                parent[pari] = parj
                min_spanning_tree += d
        return min_spanning_tree


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    a = Solution()
    print(a.solve(points))
