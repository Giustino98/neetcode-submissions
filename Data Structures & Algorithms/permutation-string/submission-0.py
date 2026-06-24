class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        L = 0
        for R in range(len(s1) - 1,len(s2)):
            if Counter(s2[L:R+1]) == s1_counter: return True
            L +=1
        return False


