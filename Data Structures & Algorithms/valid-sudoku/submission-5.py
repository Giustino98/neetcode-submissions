class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table_map = defaultdict(set)

        for idx_row,row in enumerate(board):
            for idx_column, elem in enumerate(row):
                if elem != ".":
                    if elem in table_map[("row", idx_row)]: return False
                    if elem in table_map[("column",idx_column)]: return False
                    if elem in table_map[(idx_row // 3,idx_column // 3)]: return False
                    table_map[("row", idx_row)].add(elem)
                    table_map[("column",idx_column)].add(elem)
                    table_map[(idx_row // 3,idx_column // 3)].add(elem)
        return True