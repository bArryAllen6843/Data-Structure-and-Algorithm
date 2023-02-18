# longest subsequence with limited sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/submissions/859648671/
from bisect import bisect_right
from itertools import accumulate


def answerQueries(nums, queries):
    prefix = list(accumulate(sorted(nums)))
    return [bisect_right(prefix, q) for q in queries]


if __name__ == "__main__":
    a = [4, 5, 1, 2]
    query = [3, 10, 21]
    print(answerQueries(a, query))
