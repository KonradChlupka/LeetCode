class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        counter = {0: 1}
        for i in itertools.accumulate(nums):
            if i - k in counter:
                res += counter[i - k]
            counter[i] = counter.get(i, 0) + 1
        return res
