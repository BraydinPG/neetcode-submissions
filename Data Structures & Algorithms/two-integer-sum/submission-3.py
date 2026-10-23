class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        att = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in att:
                return [att[diff], i]
            att[num] = i
        
            