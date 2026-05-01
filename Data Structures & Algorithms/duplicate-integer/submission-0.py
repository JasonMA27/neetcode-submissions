class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L1 = len(nums)
        Snum = set(nums)
        if len(Snum) == L1:
            return False
        else:
            return True
