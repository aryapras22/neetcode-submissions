class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):
            if c in seen:
                start = max(start, seen[c] + 1)
            longest = max(longest, len(s[start:i+1]))
            seen[c] = i
        
        return longest