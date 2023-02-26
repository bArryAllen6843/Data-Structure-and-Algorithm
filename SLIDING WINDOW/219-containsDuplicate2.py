class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dicto = {}
        for i, v in enumerate(nums):
            if v in dicto and i - dicto[v] <= k:
                return True
            dicto[v] = i
        return False


if __name__ == '__main__':
    num = [2,2]
    k = 3
    a = Solution()
    print(a.containsNearbyDuplicate(num, k))
