class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        word1_count_map = {}
        for char in s:
            word1_count_map[char] = word1_count_map.get(char, 0) + 1
        for char in t:
            if word1_count_map.get(char) is not None: word1_count_map[char] -= 1
        for occurence in word1_count_map.values():
            if occurence != 0: return False
        return True