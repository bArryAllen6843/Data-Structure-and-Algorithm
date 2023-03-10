class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for element in stack:
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 0, 4, 2]
    a = Solution()
    print(a.nextGreaterElement(nums1, nums2))
