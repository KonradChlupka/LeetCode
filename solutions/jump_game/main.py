class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_pos = -1
        for i in reversed(range(len(nums) - 1)):
            if zero_pos == -1 and nums[i] == 0:
                zero_pos = i
            elif zero_pos != -1 and nums[i] > zero_pos - i:
                zero_pos = -1
        return zero_pos == -1
