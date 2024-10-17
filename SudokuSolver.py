from typing import List
"""
Write a program to solve a Sudoku puzzle by filling the empty cells. 
A Sudoku solution must satisfy all of the following rules: 
- Each of the digits 1-9 must occur exactly once in each row. 
- Each of the digits 1-9 must occur exactly once in each column. 
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the 
grid. 
 
Example Board: 
[["5","3",".",".","7",".",".",".","."] 
 ["6",".",".","1","9","5",".",".","."] 
 [".","9","8",".",".",".",".","6","."] 
 ["8",".",".",".","6",".",".",".","3"] 
 ["4",".",".","8",".","3",".",".","1"] 
 ["7",".",".",".","2",".",".",".","6"] 
 [".","6",".",".",".",".","2","8","."] 
 [".",".",".","4","1","9",".",".","5"] 
 [".",".",".",".","8",".",".","7","9"]] 

"""


def solveSudoku(board: List[List[str]]) -> None:
    numBoard = dict()

    # Gather all the numbers in the board
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != '.':
                subBox_i = i // 3
                subBox_j = j // 3
                if board[i][j] not in numBoard:
                    numBoard[board[i][j]] = [[i, j, [subBox_i, subBox_j]]]
                else: # Append to the list of the key
                    numBoard[board[i][j]].append([i, j, [subBox_i, subBox_j]])
    
    solve(0, board, numBoard)
    print(board)

def solve(cellNo : int, board: List[List[str]], numBoard: dict) -> bool:
    # Base case if the row is 9 and the col is 0
    if cellNo == 81:
        return True

    row = cellNo // 9
    col = cellNo % 9
    
    # If the current cell is not empty, skip it
    if board[row][col] != '.':
        return solve(cellNo + 1, board, numBoard)

    # If the current cell is empty, try to fill it
    for num in range(1, 10):
        val = str(num)
        subBox_i = row // 3
        subBox_j = col // 3
        box_index = [subBox_i, subBox_j]

        can_place = True
        if val in numBoard:
            for pos in numBoard[val]:
                # Check if the number is in the same row, column, or box
                if pos[0] == row or pos[1] == col or pos[2] == box_index:
                    can_place = False
                    break

        # if its a valid move set the cell to the number
        if can_place:
            board[row][col] = val
            
            # Update the numBoard dictionary if the number is not in the dictionary; otherwise append to the list
            if val not in numBoard:
                numBoard[val] = [[row, col, box_index]]
            else:
                numBoard[val].append([row, col, box_index])
        
            if solve(cellNo + 1, board, numBoard):
                return True
        
        # If the number cannot be placed, backtrack
        board[row][col] = '.'

        # If the number position is in the dictionary, remove the cell from the list
        if [row, col, box_index] in numBoard[val]:
            numBoard[val].remove([row, col, box_index])

    return False
    


def main():
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
             
    solveSudoku(board)



if __name__ == "__main__":
    main()
