class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map={}
        for index, char in enumerate(s):
            if char in char_map:
                char_map[char] = -1
            else:
                char_map[char] = index
        
        for key, value in char_map.items():
            if value != -1:
                return value  
        return -1