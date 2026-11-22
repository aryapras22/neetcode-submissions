class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # what i see here are every that true are have same number of characters. so i must calculate for each string and then compare the calculation for each characters

        if len(s) != len(t):
            return False
        s_hash = {}
        for char in list(s):
            if s_hash.get(char) != None:
                s_hash[char] = s_hash.get(char, 0) + 1
            else:
                s_hash[char] = 0

        t_hash = {}
        for char in list(t):
            if t_hash.get(char) != None:
                t_hash[char] = t_hash.get(char, 0) + 1
            else:
                t_hash[char] = 0
        
        for key, value in s_hash.items():
            if  t_hash.get(key) == None:
                return False
            elif t_hash.get(key) != value:
                return False
        
        return True
            