from collections import deque


class Solution:
    def findCircleNum(self, isConnected) -> int:
        vis = set()
        n = len(isConnected)
        count = 0

        for i in range(n):
            if i in vis:
                continue
            count += 1

            vis.add(i)
            q = deque([i])
            while q:
                el = q.pop()
                for adjel in range(n):
                    if isConnected[el][adjel] and adjel not in vis:
                        vis.add(adjel)
                        q.appendleft(adjel)
        return count


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    a = Solution()
    print(a.findCircleNum(isConnected))
