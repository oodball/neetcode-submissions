class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique = len(list(set(nums)))

        if len(nums) > unique:
            return True
        return False
        