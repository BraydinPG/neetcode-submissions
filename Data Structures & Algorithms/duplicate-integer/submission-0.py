class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countNum = {}
        for num in nums:
            if num not in countNum:
                countNum[num] = 1
            else:
                return True
        return False