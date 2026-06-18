from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        occ_dict = defaultdict(int)

        for elem in s:
            occ_dict[elem] = occ_dict[elem] + 1

        for elem in t:
            if occ_dict[elem] != 0: occ_dict[elem] = occ_dict[elem] - 1

        if sum(list(occ_dict.values())) == 0: return True
        return False