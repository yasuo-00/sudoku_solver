import reader

class Board:

    def __init__(self, filename):
        self.__board=reader.read_sudoku_board_from_csv(filename)
        print(self.__board)

    def next_available_space(self):
        for row in range(self.__board.size):
            for col in range(self.__board.size):
                if self.__board[row][col]==0:
                    return (row,col)
        
        return (None,None)

    @property
    def size(self):
        return len(self.__board)

    def board_at(self, pos):
        return self.__board[pos[0]][pos[1]]
    
    @property
    def board(self):
        return self.__board
    