from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def calculate_area(r:int,c:int) -> int:
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            q = deque()
            q.append((r,c))
            area = 1
            
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1 and (row,col) not in visited:
                        visited.add((row,col))
                        area += 1
                        q.append((row,col))
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    max_area = max(max_area,calculate_area(r,c))
        
        return max_area


