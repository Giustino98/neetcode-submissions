class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # 1. Popoliamo la frequenza iniziale per s1 e per il primo blocco di s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # 2. Calcoliamo i "matches" iniziali su 26 lettere
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # 3. Facciamo scorrere la finestra a dimensione fissa su s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True
                
            # --- ELEMENTO CHE ENTRA A DESTRA ---
            r_idx = ord(s2[r]) - ord('a')
            s2_count[r_idx] += 1
            if s1_count[r_idx] == s2_count[r_idx]:
                matches += 1
            elif s1_count[r_idx] + 1 == s2_count[r_idx]:
                matches -= 1
                
            # --- ELEMENTO CHE ESCE A SINISTRA ---
            l_idx = ord(s2[l]) - ord('a')
            s2_count[l_idx] -= 1
            if s1_count[l_idx] == s2_count[l_idx]:
                matches += 1
            elif s1_count[l_idx] - 1 == s2_count[l_idx]:
                matches -= 1
                
            l += 1
            
        return matches == 26