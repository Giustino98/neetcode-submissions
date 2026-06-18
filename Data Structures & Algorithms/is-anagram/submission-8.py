from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        count = Counter(s)
        for char in t:
            if count[char] == 0:
                return False
            count[char] -= 1
            
        return True