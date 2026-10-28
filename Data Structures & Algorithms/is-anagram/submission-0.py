class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}

        for i, n, in enumerate(s):
            if n in maps:
                maps[n] += 1
            else:
                maps[n] = 1
        for i, n in enumerate(t):
            if n in mapt:
                mapt[n] += 1
            else:
                mapt[n] = 1
        
        if maps == mapt:
            return True
        return False
        