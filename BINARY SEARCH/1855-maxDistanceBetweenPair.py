class Solution:
    def maxDistance(self, nums1, nums2) -> int:
        # use first loop with 2 pointer implementation in which use one more loop with binary search algo.
        # Now first loop provides a target element to nums2 and we have to look for a maximum distance
        # between a pair (i,j) such that j is the maximum possible index where nums1[i]<=nums2[j]
        # (both the lists are non increasing).
        # So BRUTE FORCE can be if I search for every index j which is greater than or equal to i but here I am using
        # binary search to calculate a index mid such that mid is the nearest maximum index from target
        # (nearest becoz the list is in decreasing order)
        dis = 0
        max_dis = 0
        i = j = 0
        while i < len(nums1):
            target = nums1[i]
            left = i
            right = len(nums2)-1
            while left <= right:
                mid = (left + right) // 2
                if target>nums2[left]:
                    break
                elif target > nums2[mid]:
                    right = mid - 1
                # found the greater element than target in nums2 but we have to check if there exists nearest greater
                # element becoz that will be at maximum distance from target. That's why checking mid+1
                # Also mid+1 will not support in edge case where index is out of range(mid+1 does not exist)
                # So our mid is at last index then we have to return mid
                elif target <= nums2[mid] and target <= nums2[mid + 1] if mid + 1 <= right else False:
                    left = mid + 1
                # If the mid is found with nearest greater element then calculate distance and break the loop
                else:
                    j = mid
                    dis = j - i
                    left=mid+1
                    right=mid-1
            # update maximum distance
            max_dis = max(max_dis, dis)
            i += 1
        return max_dis


if __name__ == '__main__':
    nums1 = [55, 30, 5, 4, 2]
    nums2 = [100, 20, 10, 10, 5]
    a = Solution()
    print(a.maxDistance(nums1, nums2))
