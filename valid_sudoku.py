from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boards = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boards[(i//3, j //3)]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boards[(i//3,j//3)].add(board[i][j])
        
        return  True


if __name__ == "__main__":
    solution = Solution()
    board=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]

    print(solution.isValidSudoku(board))


























