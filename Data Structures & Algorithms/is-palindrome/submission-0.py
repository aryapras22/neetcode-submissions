class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_text = ""
        for letter in s:
            if letter.isalnum():
                new_text += letter.lower()
        return new_text == new_text[::-1]