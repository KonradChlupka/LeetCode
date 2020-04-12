class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = collections.deque(sorted(stones))
        while len(stones) > 1:
            diff = abs(stones.pop() - stones.pop())
            if diff:
                bisect.insort(stones, diff)
        if not stones:
            return 0
        return stones[0]
