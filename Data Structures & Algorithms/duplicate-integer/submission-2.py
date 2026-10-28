class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique = len(list(set(nums)))

        print(unique)
        print(len(nums))

        if len(nums) > unique:
            return True
        return False
        