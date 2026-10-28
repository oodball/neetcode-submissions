class Solution:
    # edge case
    # heights are equal
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxwater = (j - i) * min(heights[i], heights[j])

        while i != j:
            volume =  (j - i) * min(heights[i],heights[j])
            maxwater = max(volume, maxwater)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxwater