class Solution:
    def findDifference(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        for i in range(len(nums2)):
            if nums2[i] in set1:
                set1.remove(nums2[i])
        for j in range(len(nums1)):
            if nums1[j] in set2:
                set2.remove(nums1[j])
        return [list(set1), list(set2)]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    a = Solution()
    print(a.findDifference(nums1, nums2))
