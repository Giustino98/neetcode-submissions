from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        not_rotted = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    not_rotted += 1


        def rotte(r:int,c:int) -> int:
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            rotted = 0
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                    grid[row][col] = 2
                    q.append((row,col))
                    rotted +=1
            return rotted
                
        minutes = 0
        rotted = 0
        while q: 
            tmp_rotted = 0
            for _ in range(len(q)):
                r,c = q.popleft()
                tmp_rotted += rotte(r,c)
            rotted += tmp_rotted
            if tmp_rotted != 0: minutes += 1
        
        return minutes if rotted == not_rotted else -1



        
