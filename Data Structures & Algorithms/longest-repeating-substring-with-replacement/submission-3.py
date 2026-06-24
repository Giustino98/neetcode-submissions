'''
AAABABB k = 1

1 - L = 0 R = 0 A 
2 - L = 0 R = 1 A
3 - L = 0 R = 2 B , lo trasformo in A -> k = 0
4 - L = 0 R = 3 B 


'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        freq_map = defaultdict(int)
        output = 0

        for R in range(len(s)):
            freq_map[s[R]] += 1
            while R-L+1 > max(freq_map.values(), default = 0) + k:
                freq_map[s[L]] -= 1
                L += 1

            output = max(output,sum(freq_map.values()))
        
        return output
