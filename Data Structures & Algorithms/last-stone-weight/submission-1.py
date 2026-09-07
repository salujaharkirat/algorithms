import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            first, second = abs(heapq.heappop(heap)), abs(heapq.heappop(heap))
            if second < first:
                heapq.heappush(heap, -(first - second))
        
        if not heap:
            return 0
        return abs(heap[0])
        