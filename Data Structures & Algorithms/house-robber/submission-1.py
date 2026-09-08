from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        def traverse(pos):
            if pos in memo:
                return memo[pos]

            if pos == 0:
                return nums[0]
            if pos == 1:
                return max(nums[0], nums[1])

            memo[pos] = max(traverse(pos - 2) + nums[pos], traverse(pos - 1))
            return memo[pos]

        return traverse(len(nums) - 1)