class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        min_length = min(len(word1), len(word2))


        for i in range(min_length):
            merged += word1[i]
            merged += word2[i]

        

        print(word2[min_length::])

        if len(word1) > len(word2):
            merged += word1[min_length::]

        if len(word2) > len(word1):
            print(word2[min_length::])
            merged += word2[min_length::]

        return merged
        