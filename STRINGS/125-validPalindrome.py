class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_string = ""
        backward_string = ""

        for letter in s.lower():
            if letter != " " and letter != "," and letter != ":":
                forward_string = forward_string + letter
                backward_string = letter + backward_string
        if backward_string == forward_string:
            return 1
        return 0


if __name__ == '__main__':
    # st = 'A man, a plan, a canal: Panama'
    st = 'a.'
    a = Solution()
    print(a.isPalindrome(st))
