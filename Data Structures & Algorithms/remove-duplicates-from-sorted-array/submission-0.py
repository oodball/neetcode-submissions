class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique = []

        i = 0

        while i in range(len(nums)):
            print(nums[i])
            print(unique)
            if nums[i] not in unique:
                unique.append(nums[i])
                i += 1
            else:
                nums.pop(i)
        return len(nums)
                
        