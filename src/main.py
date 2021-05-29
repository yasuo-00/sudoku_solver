from ast import parse
import reader
import argparse
from classes.board import Board
from classes.graph import Graph

parser = argparse.ArgumentParser(description='Sudoku Solver')
parser.add_argument('-f', '--filename', type=str, metavar='filename', help='Input sudoku solver csv filename')
args = parser.parse_args()


def main(args):

    board = Board(args.filename)
    sudoku_graph = Graph(board)
    sudoku_graph.init_nodes(board)
    sudoku_graph.set_adj_nodes(board)



if __name__=='__main__':
    main(args)
