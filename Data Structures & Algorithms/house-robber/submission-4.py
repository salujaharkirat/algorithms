from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]
        # memo = defaultdict(int)

        # def traverse(pos):
        #     if pos in memo:
        #         return memo[pos]

        #     if pos == 0:
        #         return nums[0]
        #     if pos == 1:
        #         return max(nums[0], nums[1])

        #     memo[pos] = max(traverse(pos - 2) + nums[pos], traverse(pos - 1))
        #     return memo[pos]

        # return traverse(len(nums) - 1)