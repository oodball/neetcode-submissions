class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = {}

        for i, n in enumerate(nums):
            if n in maps:
                return True
            maps[n] = i
        return False