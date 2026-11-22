class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
       letters_s = sorted(s)
       letters_t = sorted(t)

       if letters_s == letters_t: return True
       else: return False
