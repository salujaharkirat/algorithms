class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def generate(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                generate(i + 1, path)
                path.pop()
        
        generate(0, [])

        return res
        