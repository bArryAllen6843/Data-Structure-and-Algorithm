import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        ans = []
        for i in str(num):
            i = int(i)
            if i % 2:
                odd.append(-i)
                ans.append(True)
            else:
                even.append(-i)
                ans.append(False)

        heapq.heapify(odd)
        heapq.heapify(even)
        for i in range(len(ans)):
            if ans[i]:
                ans[i] = -heapq.heappop(odd)
            else:
                ans[i] = -heapq.heappop(even)

        return int("".join(str(n) for n in ans))


if __name__ == '__main__':
    num = 1234
    a = Solution()
    print(a.largestInteger(num))
