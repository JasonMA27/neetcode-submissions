class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in nums:
            nums.sort()
        return nums