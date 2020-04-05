class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for el in nums:
            if el in seen:
                seen.remove(el)
            else:
                seen.add(el)
        return seen.pop()
