class Solution:
    def successfulPairs(self, spells, potions, success: int):
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()

        for i in range(n):
            spell = spells[i]
            l = 0
            r = m - 1
            while l <= r:
                mid = (l + r) // 2
                product = spell * potions[mid]
                if product >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            pairs[i] = m - l
        return pairs


if __name__ == '__main__':
    a = Solution()
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(a.successfulPairs(spells, potions, success))
