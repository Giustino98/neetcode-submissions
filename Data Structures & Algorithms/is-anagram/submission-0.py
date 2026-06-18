class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_count_dict = {}

        if len(s) != len(t): return False

        for elem in s:
            if elem in my_count_dict:
                my_count_dict[elem] += 1
            else: my_count_dict[elem] = 1
        for elem in t:
            if elem not in my_count_dict:
                return False
            else:
                my_count_dict[elem] -= 1
        
        for value in my_count_dict.values():
            if value != 0:
                return False
        return True
        