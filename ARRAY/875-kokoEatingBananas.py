class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        def feasible(speed):
            return sum((pile - 1) // speed + 1 for pile in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    a = Solution()
    print(a.minEatingSpeed(piles, h))
