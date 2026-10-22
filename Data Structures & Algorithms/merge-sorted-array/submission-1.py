class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len2 = len(nums2)

        if len2 != 0:
            nums1[-len2:] = nums2[:len2]
            nums1.sort()



        
        