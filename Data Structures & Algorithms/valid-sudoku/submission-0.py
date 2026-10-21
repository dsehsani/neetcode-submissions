class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)  # row/col : set
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # (r//3, c//3) : set

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                # check if repetition in dictionaries
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[(i // 3, j // 3)]
                ):
                    return False
                
                # update dictionaries 
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        

        return True


                



                
