class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = {}
        hasht = {}
        for i in range(0, len(s)):
            if s[i] not in hashs:
                hashs[s[i]] = 1
            else:
                hashs[s[i]] += 1
        for j in range(0, len(t)):
            if t[j] not in hasht:
                hasht[t[j]] = 1
            else:
                hasht[t[j]] += 1
        print(hashs)
        print(hasht)
        return hashs == hasht

        