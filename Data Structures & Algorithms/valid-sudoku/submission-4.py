from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_dict = defaultdict(set)

        for i in range(0, len(board)):
            for j, elem in enumerate(board[i]):
                if elem == ".": continue
                if elem  in sudoku_dict[("colum", j)]: return False
                else: sudoku_dict[("colum", j)].add(elem)
                if elem in sudoku_dict[("row", i)]: return False
                else: sudoku_dict[("row", i)].add(elem)
                if elem in sudoku_dict[("square", (i//3)*3 + (j//3))]: return False
                else: sudoku_dict[("square", (i//3)*3 + (j//3))].add(elem)

        print(sudoku_dict)
        return True