from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occurences = defaultdict(list)
        res = []
        for string in strs:
            alph = [0] * 26
            for char in string:
                alph[ord(char) - ord("a")] +=1
            occ_key = tuple(alph)
            occurences[occ_key].append(string)
        
        for bucket in occurences.values():
            res.append(bucket)
        return res
