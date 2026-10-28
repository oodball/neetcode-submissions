class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        maps = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in maps:
                return[maps[diff], i]
            maps[n] = i

        