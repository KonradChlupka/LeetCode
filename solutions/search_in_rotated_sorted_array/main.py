class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < nums[end]:
                if nums[middle] < target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if nums[start] <= target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
        return -1
