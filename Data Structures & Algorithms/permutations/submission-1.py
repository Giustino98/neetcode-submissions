class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(subset: List[int]) -> None:
            # 1. Caso base: se la permutazione è completa, la salviamo e risaliamo
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            # 2. Giriamo su tutti i candidati possibili
            for elem in nums:
                if elem not in subset:
                    subset.append(elem)   # Fai la scelta
                    backtrack(subset)     # Esplora le conseguenze
                    subset.pop()          # Torna indietro (Backtrack!)
        
        backtrack([])
        return res