class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        first = strs[0]
        last = strs[-1]

        longest = ""

        for i in range (len(first)):
            print(first[i])
            print(last[i])
            if first[i] == last[i]:
                longest = longest + first[i]
            else:
                return longest

        return longest
        
        