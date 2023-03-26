from collections import Counter


class Solution:
    def getHint(self, secret, guess):
        bulls = sum([x == y for x, y in zip(secret, guess)])
        Count_sec = Counter(secret)
        Count_gue = Counter(guess)

        bulls_cows = sum([min(Count_gue[ele], Count_sec[ele]) for ele in Count_sec])

        return str(bulls) + "A" + str(bulls_cows - bulls) + "B"


if __name__ == '__main__':
    secret = "1807"
    guess = "7810"
    a = Solution()
    print(a.getHint(secret, guess))
