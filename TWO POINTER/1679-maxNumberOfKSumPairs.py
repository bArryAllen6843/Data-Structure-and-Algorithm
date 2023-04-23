from collections import Counter


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        # TWO POINTER
        # nums.sort()
        # l = 0
        # r = len(nums)-1
        # ans = 0
        # while l<r:
        #     if nums[r]+nums[l]==k:
        #         ans+=1
        #         l+=1
        #         r-=1
        #     elif nums[r]+nums[l]>k:
        #         r-=1
        #     else:
        #         l+=1

        # return ans

        # HASHMAP
        cnt, ans = Counter(nums), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans // 2


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    k = 5
    a = Solution()
    print(a.maxOperations(nums, k))
