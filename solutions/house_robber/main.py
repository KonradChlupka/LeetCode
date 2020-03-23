class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums + [0])

        without_current = 0
        best = nums[0]

        for i in range(1, len(nums)):
            without_prev, without_current = without_current, best
            best = max(nums[i] + without_prev, without_current)
        return best
