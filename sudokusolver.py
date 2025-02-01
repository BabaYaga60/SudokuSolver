sboard = [
    [0, 1, 0, 7, 0, 0, 9, 3, 0],
    [6, 9, 0, 0, 0, 2, 0, 1, 7],
    [0, 0, 0, 0, 0, 6, 8, 2, 4],
    [2, 6, 0, 0, 7, 8, 0, 4, 0],
    [5, 8, 1, 4, 0, 9, 0, 7, 0],
    [0, 7, 0, 5, 6, 1, 0, 0, 8],
    [0, 3, 5, 0, 0, 0, 7, 0, 2],
    [7, 0, 0, 6, 1, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
]

def possible_value(board, row, col):
    used_in_row = set()
    used_in_col = set()
    used_in_box = set()
    
    for i in range(9):
        sayx = board[row][i]
        if sayx != 0:
            used_in_row.add(sayx)

    for j in range(9):
        sayy = board[j][col]
        if sayy != 0:
            used_in_col.add(sayy)

    boxbx = 3 * (row // 3)
    boxby = 3 * (col // 3)
    
    for x in range(boxbx, boxbx + 3):  
        for y in range(boxby, boxby + 3):  
            sayb = board[x][y]
            if sayb != 0:
                used_in_box.add(sayb)

    used_numbers = used_in_row.union(used_in_col, used_in_box)
    
    return [num for num in range(1, 10) if num not in used_numbers]

def adding_with_logic(board):
    while True:
        değer = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    val = possible_value(board, i, j)
                    if len(val) == 1:
                        board[i][j] = val[0]
                        değer = True
        if not değer:
            break
    if not is_solved(board):
        backtracking_starting_and_continues_with_best_empty_cells(board)

def best_emptyies_sorted(board):
    diction = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                diction[(i, j)] = len(possible_value(board, i, j))
    
    keys = list(diction.keys())
    keys.sort(key=lambda k: diction[k]) 
    
    return keys

def backtracking_starting_and_continues_with_best_empty_cells(board):
    empty_cells = best_emptyies_sorted(board)
    if len(empty_cells) == 0:
        return True 
    
    row, col = empty_cells[0]  
    
    for num in possible_value(board, row, col):
        board[row][col] = num
        
        if backtracking_starting_and_continues_with_best_empty_cells(board):
            return True
        
        board[row][col] = 0 

    return False

def is_solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

adding_with_logic(sboard)

if is_solved(sboard):
    print("\nÇözülen Sudoku tahtası:")
    print_board(sboard)
else:
    print("\nSudoku çözülemedi!")
