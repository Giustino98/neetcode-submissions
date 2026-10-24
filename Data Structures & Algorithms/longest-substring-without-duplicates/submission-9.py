class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        l = 0
        res = 0
        for r in s:
            while r in longest:
                longest.remove(s[l])
                l += 1
            longest.add(r)
            res = max(res,len(longest))
        
        return res
