class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        print(stones)
        if not stones:
            return 0

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(-x - -y))
                print(x, y, x - y, stones)
            else:
                continue
        if not stones:
            return 0
        else:
            return heapq.heappop(stones) * -1


        