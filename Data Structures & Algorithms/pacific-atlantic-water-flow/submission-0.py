from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        
        ROWS, COLS = len(heights), len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()
        
        # 1. Popoliamo i set di partenza con i bordi (esattamente come hai fatto tu)
        for c in range(COLS):
            visited_pacific.add((0, c))
            visited_atlantic.add((ROWS - 1, c))
        for r in range(ROWS):
            visited_pacific.add((r, 0))
            visited_atlantic.add((r, COLS - 1))

        # 2. La BFS ora accetta TUTTI i punti di partenza dell'oceano insieme
        def bfs(ocean_visited_set: set) -> None:
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            # Inizializziamo la coda direttamente con TUTTI i bordi di quell'oceano
            q = deque(ocean_visited_set) 

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # IL PARACADUTE COMPLETO: Confini + Regola Altezza + NON ANCORA VISITATO
                    if (0 <= new_row < ROWS and 
                        0 <= new_col < COLS and 
                        heights[new_row][new_col] >= heights[row][col] and 
                        (new_row, new_col) not in ocean_visited_set):
                        
                        ocean_visited_set.add((new_row, new_col))
                        q.append((new_row, new_col))

        # 3. Facciamo partire SOLO DUE grandi ondate
        bfs(visited_pacific)
        bfs(visited_atlantic)

        # 4. Troviamo l'intersezione (Il tuo ciclo finale, perfetto)
        output_cells = []
        for elem in visited_atlantic:
            if elem in visited_pacific:
                output_cells.append([elem[0], elem[1]])
                
        return output_cells