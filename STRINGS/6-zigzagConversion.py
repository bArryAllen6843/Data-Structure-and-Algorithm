class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        p = [''] * numRows
        index, step = 0, 1

        for x in s:
            p[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(p)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    a = Solution()
    print(a.convert(s, numRows))
