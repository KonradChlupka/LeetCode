class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float("inf")
        best = 0

        for price in prices:
            if price < smallest:
                smallest = price
            if price > best:
                best = max(best, price - smallest)
        return best
