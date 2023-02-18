# method-1 (worst in time and space)

def intersection1(nums1, nums2):
    hashmap = {}
    s = set()

    for i in range(len(nums1)):
        hashmap[nums1[i]] = i

    for n in nums2:
        if n in hashmap:
            s.add(n)
    return s


# method-2 (best method)

def intersection2(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    if m < n:
        nums1, nums2 = nums2, nums1
        m, n = n, m

    nums1.sort()
    nums2.sort()

    i, j = 0, 0

    ans = set()
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            ans.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return list(ans)


# method-3 (this method only saves memory not good in time)
def intersection3(nums1, nums2):
    l = []
    for i in nums1:
        if i in nums2 and i not in l:
            l.append(i)
    return l


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
print(intersection2(nums1, nums2))
