import numpy as np

def read_sudoku_board_from_csv(filename):
    file = open(filename)
    matrix = np.loadtxt(file, delimiter=';', dtype=int)
    return matrix

def read_sudoku_board_from_terminal():
    pass