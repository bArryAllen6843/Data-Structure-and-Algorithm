class Solution:
    def magicalSubarrays(self, n: int, arr) -> int:
        cnt = 0
        for i in range(n):
            for j in range(i, n):
                sub_arr = arr[i:j + 1]
                odd_cnt = 0
                for num in sub_arr:
                    if num % 2 != 0:
                        odd_cnt += 1

                if odd_cnt % 2 == 0 and odd_cnt!=0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    n = 4
    arr = [2, 1, 2, 3]
    a = Solution()
    print(a.magicalSubarrays(n, arr))
