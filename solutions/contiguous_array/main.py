class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        level = 0
        best_dist = 0
        d = {level: -1}
        for i, num in enumerate(nums):
            level += 1 if num else -1
            if level not in d:
                d[level] = i
            else:
                best_dist = max(best_dist, i - d[level])
        return best_dist
