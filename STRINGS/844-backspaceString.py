class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(s):
            ans = []
            for i in s:
                if i != "#":
                    ans.append(i)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return solve(s) == solve(t)


if __name__ == '__main__':
    a = 'ab#c'
    b = 'ad#c'

    ss = Solution()
    print(ss.backspaceCompare(a, b))
