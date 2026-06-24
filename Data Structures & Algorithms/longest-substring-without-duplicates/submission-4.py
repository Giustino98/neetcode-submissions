class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        unique_set = set()
        res = 0

        for R in range(len(s)):
            while s[R] in unique_set:
                unique_set.remove(s[L])
                L +=1
            unique_set.add(s[R])
            res = max(res,len(unique_set))
        return res