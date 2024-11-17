WHITE_PAWN = 1
BLACK_PAWN = 7

class ChessBoard:
    #0 = empty
    #1 = pawn_white
    #2 = bishop_white
    #3 = knight_white
    #4 = rook_white
    #5 = queen_white
    #6 = king_white
    #7 = pawn_black
    #8 = bishop_black
    #9 = knight_black
    #10 = rook_black
    #11 = queen_black
    #12 = king_black





    def __init__(self, as_white = True):
        
            #The chess board is read as each sub array being a row on the chess board.
            #The start of the array is the side facing the user.
        self.chessBoard = [[4, 1, 0, 0, 0, 0, 7, 10],[3, 1, 0, 0, 0, 0, 7, 9],\
                            [2, 1, 0, 0, 0, 0, 7, 8],[5, 1, 0, 0, 0, 0, 7, 11],\
                            [6, 1, 0, 0, 0, 0, 7, 12],[2, 1, 0, 0, 0, 0, 7, 9],\
                            [3, 1, 0, 0, 0, 0, 7, 9],[4, 1, 0, 0, 0, 0, 7, 10]]
        if not as_white:
            for row in self.chessBoard:
                self.chessBoard = [row[::-1] for row in self.chessBoard]


        else:
            pass
            #Throw an exception - players colour not specified

        for i in range(7):
            self.chessBoard.append(0)
            for j in range(7):
                if j == 1:
                    self.chessBoard.append(BLACK_PAWN)
                if j == 6:
                    self.chessBoard.append(WHITE_PAWN)
                    
                self.chessBoard[i].append(0)
    
    def move(piece, prev_pos_row,prev_pos_column, new_pos_row, new_pos_column):
        #make a .get_type for each piece
        #self.chessBoard[]