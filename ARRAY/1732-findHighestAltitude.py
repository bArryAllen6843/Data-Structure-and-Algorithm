class Solution:
    # The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
    def largestAltitude(self, gain) -> int:
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
        return max(gain) if max(gain) > 0 else 0


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    a = Solution()
    print(a.largestAltitude(gain))
