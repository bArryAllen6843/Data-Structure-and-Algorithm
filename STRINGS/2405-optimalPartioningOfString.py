class Solution:
    def partitionString(self, s: str) -> int:
        h = set()
        count = 1
        for ch in s:
            if ch in h:
                count += 1
                h.clear()
                h.add(ch)
            else:
                h.add(ch)
        return count


if __name__ == '__main__':
    s = "abacaba"
    a = Solution()
    print(a.partitionString(s))
