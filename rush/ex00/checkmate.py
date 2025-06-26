import sys

#function to check if the coordinates of a chess piece are within the chessboard
def is_valid(row, col, size):
    return size > row >= 0 and size > col >= 0

#function to check if a sliding pieve (queen, bishop, rook) has a king piece as the first piece in it's path
def check_attack_dir(piece_row, piece_col, K_pos, board, size, direction):
    K_row, K_col = K_pos

    #iterate through each direction of a piece
    for direction_row, direction_col in direction:
        row, col = piece_row + direction_row, piece_col + direction_col
        
        #finds the king while the direction is within the board
        while is_valid(row, col, size):
            if board[row][col] == 'K':
                return True
            
            #break if outside of board
            elif board[row][col] != '.': 
                break
            
            #continues in the same direction
            row += direction_row
            col += direction_col
    return False

#function to check if a pawn has a king piece in it's attack path (this is a seperate function due to the pawn piece not being a sliding chess piece)
def check_pawn(pawn_row, pawn_col, K_pos, board, size):
    offset = [(-1, -1), (-1, 1)]

    #check if king is in pawn's attack path
    for direction_row, direction_col in offset:
        row, col = pawn_row + direction_row, pawn_col + direction_col

        if is_valid(row, col, size) and (row, col) == K_pos:
            return True
    return False

#main function that check for errors, king's position on the board and confirms if the king is in check
def checkmate(board_str):
    #removes whitespace from the board (because the board is multi line)
    rows = board_str.strip().split('\n')

    #checks if board is empty
    if not rows or (len(rows) == 1 and not rows[0]):
        return 
    
    board_size = -1 #-1 because board size is not inputted yet
    board = [] #list for presenting the board

    for row_str in rows:
        #skip whitespace lines
        if not row_str.strip():
            continue
    
        #determine board size from first row
        if board_size == -1:
            board_size = len(row_str)
            if board_size == 0:
                print("Error")
                return

        #checks if the amout of rows is equal to the board size
        if len(row_str) != board_size:
            print("Error")
            return

        #append the row as a list of char
        board.append(list(row_str)) 
    
    #if no board exist, return
    if not board:
        print("Error")
        return
    
    #checks if the amout of rows in the board list is equal to the board size
    if len(board) != board_size:
        print("Error")
        return
    

    K_pos = None
    K_count = 0

    #find the king's position
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 'K':
                K_pos = (row, col)
                K_count += 1

    #checks to see if king is on the chess board
    if K_count != 1:
        return
    
    #define the direction of each chess piece (exept pawn)
    R_dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    B_dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    Q_dir = R_dir + B_dir


    for row in range(board_size):
        for col in range(board_size):
            piece = board[row][col]

            #uses the attack direction function to see if king piece is in the path of any of the other pieces
            if piece == "R":
                if check_attack_dir(row, col, K_pos, board, board_size, R_dir):
                    print("Success")
                    return
            
            elif piece == "B":
                if check_attack_dir(row, col, K_pos, board, board_size, B_dir):
                    print("Success")
                    return

            elif piece == "Q":
                if check_attack_dir(row, col, K_pos, board, board_size, Q_dir):
                    print("Success")
                    return
            
            elif piece == "P":
                if check_pawn(row, col, K_pos, board, board_size):
                    print("Success")
                    return
                
    #fails if no king is found in the path
    print("Fail")
    