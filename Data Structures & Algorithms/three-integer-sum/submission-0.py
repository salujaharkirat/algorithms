class Solution:
    def findSum(self, res, left, right, nums, curr):
        while left < right:
            val = nums[curr] + nums[left] + nums[right]
            if val == 0:
                res.append([nums[curr], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif val < 0:
                left += 1
            else:
                right -= 1
        

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.findSum(res, i + 1, len(nums) - 1, nums, i)
        
        return res

        