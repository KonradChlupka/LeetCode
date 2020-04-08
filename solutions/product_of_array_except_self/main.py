class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_front = itertools.accumulate(nums[:-1], operator.mul)
        from_back = itertools.accumulate(reversed(nums[1:]), operator.mul)
        res = [1]
        res.extend(from_front)
        for i, el in enumerate(from_back):
            res[-i - 2] *= el
        return res
