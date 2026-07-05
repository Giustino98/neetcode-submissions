from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        # Una tua funzione helper (bfs o dfs) per esplorare l'intera isola
        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and \
                    grid[row][col] == "1" and (row,col) not in visited:
                        queue.append((row,col))
                        visited.add((row,col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c) # Marca tutta l'isola come visitata
                    
        return islands