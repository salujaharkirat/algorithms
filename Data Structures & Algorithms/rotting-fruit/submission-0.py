from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.appendleft((r, c))
        
        while q and fresh:
            time += 1
            len_q = len(q)

            for _ in range(len_q):
                r,c = q.pop()
                for pr, pc in [[0,1], [0,-1], [1,0],[-1,0]]:
                    if r + pr < 0 or r + pr > len(grid) - 1:
                        continue
                    if c + pc < 0 or c + pc > len(grid[0]) - 1:
                        continue
                    if grid[r+pr][c+pc] == 1:
                        q.appendleft((r + pr,c + pc))
                        grid[r+pr][c+pc] = 2
                        fresh -= 1
        
        if fresh:
            return -1
        
        return time
            
        