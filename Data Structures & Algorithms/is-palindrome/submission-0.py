class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_text = "".join(
        char for char in s 
        if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122)
        clean_text = clean_text.lower()

        i = 0
        j = len(clean_text) - 1

        print(clean_text)

        while i <= j:
            if clean_text[i] != clean_text[j]:
                return False
            i += 1
            j -= 1
        return True
        