class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # Pattern: <lunghezza> + <separatore> + <stringa>
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. Trova il separatore '#' per capire dove finisce il numero della lunghezza
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Estrai la lunghezza e convertila in intero
            length = int(s[i:j])
            
            # 3. La stringa vera e propria inizia subito dopo '#' (j + 1)
            # e finisce dopo 'length' caratteri
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. Muovi il puntatore all'inizio del prossimo blocco
            i = end
            
        return res