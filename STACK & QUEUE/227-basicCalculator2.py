class Solution:
    def calculate(self, s):
        num, st, sign = 0, [], '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    st.append(num)
                elif sign == "-":
                    st.append(-num)
                elif sign == "*":
                    st.append(st.pop() * num)
                elif sign == "/":
                    st.append(int(st.pop() * num))
                num = 0
                sign = s[i]
        return sum(st)


if __name__ == '__main__':
    s = "3+2*2"
    # s = " 3+5 / 2 "
    a = Solution()
    print(a.calculate(s))
