class Solution:
    # BRUTE FORCE
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if n == 0: return False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1
                if n == 0:
                    return True
                flowerbed[i] = 1
        return False

    # IMPROVED METHOD USING PREFIX AND SUFFIX ZEROES
    def canPlaceFlowers1(self, flowerbed, n: int) -> bool:
        # added a zero at prefix position that's why zeroes is 1 initially
        zeroes, ans = 1, 0
        # if there are consecutive zeroes in odd number then a one can be placed according to number of zeroes
        # now we don't have to check prefix and suffix zeroes as we have added dummy zeroes to start and end
        for f in flowerbed:
            if f == 0:
                zeroes += 1
            else:
                ans += (zeroes - 1) // 2
                zeroes = 0
        return ans + zeroes // 2 >= n


if __name__ == '__main__':
    flowerbed = [1, 0, 1, 0, 1]
    n = 1
    a = Solution()
    print(a.canPlaceFlowers1(flowerbed, n))
