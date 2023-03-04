class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums2[j] > nums1[i]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    a = Solution()
    print(a.intersect(nums1, nums2))
