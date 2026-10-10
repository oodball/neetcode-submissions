class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters = {}
        lettert = {}

        for char in s:
            if char not in letters:
                letters[char] = 1
            elif char in letters:
                letters[char] += 1

        for char in t:
            if char not in lettert:
                lettert[char] = 1
            elif char in lettert:
                lettert[char] += 1

        print(letters)
        print(lettert)

        return letters == lettert


        