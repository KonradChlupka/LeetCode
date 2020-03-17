class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        best_now = best = nums[0]
        for i in range(1, len(nums)):
            best_now = max(nums[i], best_now + nums[i])
            best = max(best, best_now)
        return best