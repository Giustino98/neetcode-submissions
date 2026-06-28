"""
s = "abcacbopqrst"

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = {}
        l = 0
        max_length = 0

        for r in range(len(s)):
            if s[r] in unique_chars:
                l = max(l,unique_chars[s[r]] + 1)
            unique_chars[s[r]] = r
            max_length = max(max_length, r-l+1)
        return max_length