class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()

        mid= (len(nums))//2
        print(mid)
        print(nums)

        return nums[mid]
        