from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS,COLS = len(grid), len(grid[0])
        max_area = 0

        def calculate_area(r,c):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            area = 1
            queue = deque()
            queue.append((r,c))
            while queue:
                row,col = queue.popleft()
                for dx,dy in directions:
                    new_row,new_col = row + dx, col + dy
                    if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 1 and (new_row,new_col) not in visited:
                        area += 1
                        visited.add((new_row,new_col))
                        queue.append((new_row,new_col))
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    max_area = max(max_area,calculate_area(r,c))
        
        return max_area
                    

