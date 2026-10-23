class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        attempts = {}
        i, j = 0, 1
        while j <= len(nums)-1:
            if nums[i] + nums[j] == target:
                return [i] + [j]
            elif j == len(nums) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        
        
            