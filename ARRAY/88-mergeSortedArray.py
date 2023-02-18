# def merge(nums1, m, nums2, n):
#     p1, p2 = 0, 0
#     while nums1[p1] != 0:
#         p1 += 1
#     while p2 != n:
#         nums1[p1] = nums2[p2]
#         p1 += 1
#         p2 += 1
#
#     nums1.sort()
#     return nums1

def merge1(nums1, m, nums2, n):
    while n:
        if m and nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    return nums1


if __name__ == '__main__':
    a = [1, 2, 3]
    a_len = len(a)
    b = [2, 5, 6]
    b_len = len(b)
    print(merge1(a, a_len, b, b_len))
