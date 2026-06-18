class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for elem in strs:
            occurrences = [0] * 26
            for ch in elem:
                occurrences[ord(ch) - ord("a")] += 1
            
            tuple_occurrences = tuple(occurrences)
            if tuple_occurrences in res: res[tuple_occurrences].append(elem)
            else: res[tuple_occurrences] = [elem]

        output = []
        for bucket in res.values():
            output.append(bucket)
        return output