class Solution:
    # BRUTE-FORCE APPROACH
    # For each house, we have two choices -
    # 1. Dont rob the house and move to next house.
    # 2. Rob the house and move to the house after next house (We dont move directly to next house because we
    # can rob adjacent houses).
    # Time Complexity : O(2N), where N is the number of elements in A. At each index, we have two choices of either
    # robbing or not robbing the current house. Thus this leads to time complexity of 2*2*2...n times ≈ O(2N)
    # Space Complexity : O(N), required by implicit recursive stack. The max depth of recursion can go upto N

    def rob(self, A, i=0):
        return max(self.rob(A, i + 1), A[i] + self.rob(A, i + 2)) if i < len(A) else 0
    #                         OR
    # def rob(self, A, i=0):
    #     if i < len(A):
    #         # print current index i and the subarray A[i:]
    #         print("i:", i, "A[i:]", A[i:])
    #         # recursively call rob function for the next index i+1 and i+2
    #         rob_next = self.rob(A, i + 1)
    #         rob_next_next = self.rob(A, i + 2)
    #         # calculate the maximum value between rob_next and rob_next_next plus the current index value
    #         max_value = max(rob_next, A[i] + rob_next_next)
    #         # print the maximum value and return it
    #         print("max_value:", max_value)
    #         return max_value
    #     else:
    #         # base case: return 0 when the index is out of bounds
    #         return 0

    # Dynamic Programming - Tabulation
    # We can implement the same logic as above in an iterate approach as well. Here, we again use a dp array to save
    # the results of computation. In this case, dp[i] will denote maximum loot that we can get by considering till
    # ith index. At every index,
    # 1. We can keep same loot as we had at previous index - dp[i-1]
    # 2. we can rob the current house and add it to the loot we have at i-2th index - A[i] + dp[i-2]
    # Time Complexity : O(N), just single iteration is performed from 2 to N to compute each dp[i].
    # Space Complexity : O(N), required for dp
    def rob1(self, A):
        if len(A) == 1: return A[0]

        dp = [*A]
        dp[1] = max(dp[0], dp[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i - 2] + A[i], dp[i - 1])
        return dp[-1]

    # Space-Optimzed Dynamic Programming
#     We can observe that the above dp solution relied only on the previous two indices in dp to compute the value of
#     current dp[i]. So, we dont really need to maintain the whole dp array and can instead just maintain the values of
#     previous index (denoted as prev below) and previous-to-previous index (denoted as prev2) and we can calculate the
#     value for current index (cur) using just these two variables and roll-forward each time.
    def rob2(self,A):
        prev2,prev,cur=0,0,0
        for i in A:
            cur=max(prev2+i,prev)
            prev2=prev
            prev=cur
        return cur

if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    a = Solution()
    print(a.rob(nums))
    print(a.rob1(nums))
    print(a.rob2(nums))
