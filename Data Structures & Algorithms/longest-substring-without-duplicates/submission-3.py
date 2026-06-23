class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "": return 0

        L = 0
        R = 1

        substr = {s[L]}
        max_count = len(substr)

        while (R < len(s)):
            while s[R] in substr:
                substr.remove(s[L])
                L += 1
            else: 
                substr.add(s[R])
            max_count = max(max_count,len(substr))
            R += 1
        return max_count

            
        