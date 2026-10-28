class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0 or len(nums) == 1:
            return False
        newhash = []

        for i in nums:
            if i not in newhash:
                newhash.append(i)
            else:
                return True
        return False
        
         