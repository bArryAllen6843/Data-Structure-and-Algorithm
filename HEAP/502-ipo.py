import heapq


class Solution:
    def f(self, k, w, profits, capital):
        n = len(profits)
        project = [(capital[i], profits[i]) for i in range(n)]
        i = 0
        heap = []
        while k > 0:
            while i < n and project[i][0] <= w:
                heapq.heappush(heap, -project[i][1])
                i += 1
            if not heap:
                break
            w -= heapq.heappop(heap)
            k -= 1
        return w


if __name__ == '__main__':
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    a = Solution()
    print(a.f(k, w, profits, capital))
