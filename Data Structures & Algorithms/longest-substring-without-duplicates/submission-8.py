"""
s = "abcacbopqrst"

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unique_characters = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in unique_characters:
                unique_characters.remove(s[l])
                l+=1
            unique_characters.add(s[r])
            max_length = max(max_length,len(unique_characters))
        return max_length