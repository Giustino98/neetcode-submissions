#stessi principi della ricerca binaria classica ma in 2d
"""
quanti indici e cambia il concetto di punto medio?
posso vedere la matrice come un lungo array
l'elemento (1,0) è in realtà il quinto elemento
quindi l = 0
r = (m*n) - 1
m = l + (r-l) // 2 
poi faccio modulo m e ottengo l'indice di riga, modulo n e ottengo l'indice
di colonna
quindi confronto m con le coppie e aggiorno sempre con i moduli
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1 #m*n 3*4

        while l<=r:
            m = l + (r-l) // 2
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                l = m + 1
            else:
                r = m - 1

        return False
