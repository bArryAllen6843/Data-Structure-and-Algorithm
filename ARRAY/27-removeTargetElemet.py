def removeElement(nums, val: int) -> int:
    nums.sort()
    n = len(nums)
    p, c = 0, n - 1
    if nums:
        while nums[p] != val:
            # if val is not there in the nums
            if p == n - 1:
                return p + 1
            p += 1

        if nums[c] == val:
            return p
        else:
            while nums[p] == val:
                if p != c:
                    nums[p] ,nums[c]= nums[c],nums[p]
                    p += 1
                    c -= 1
                else:
                    return p
            if p>c:
                return p
            elif p==c:
                return p+1
    return -1


if __name__ == "__main__":
    # p = [0, 1, 2, 2, 3, 0, 4, 2]
    # p = [0, 1, 4, 7, 3, 0, 4, 8]  # list with no val
    # p=[]  # empty list and val=0
    # p=[2]  # list with only one element lets say 2 and val=3
    # p = [4, 5]  # val=4
    p=[2,3,3]  # val=2
    print(removeElement(p, 2))
