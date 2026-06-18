class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        chars_dict = defaultdict(int)

        for char in s:
            chars_dict[char] += 1

        for char in t:
            chars_dict[char] -= 1

        return len(set(chars_dict.values())) == 1