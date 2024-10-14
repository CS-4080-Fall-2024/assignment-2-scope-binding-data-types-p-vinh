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
    
    # [print(f"{key}: {value}") for key, value in numBoard.items()]

    # Use backtracking to solve the board and the numBoard dictionary to keep track of the numbers/check
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == '.':
                subBox_i = i // 3
                subBox_j = j // 3
                for num in range(1, 10):
                    if [i, j, [subBox_i, subBox_j]] not in numBoard[str(num)]:
                        board[i][j] = str(num)
                        numBoard[str(num)] = [[i, j, [subBox_i, subBox_j]]]
                        break
                    else:
                        board[i][j] = '.'
                        continue
    
    print(board)




    


def main():
    solveSudoku([["5","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]])

if __name__ == "__main__":
    main()
