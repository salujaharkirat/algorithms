class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        res = 2

        for _ in range(3, n + 1):
            res = first + second
            first = second
            second = res
        
        return res


        # if n == 0:
        #     return 0

        # if n == 1:
        #     return 1
        
        # if n == 2:
        #     return 2

        # return self.climbStairs(n - 1) + self.climbStairs(n-2)