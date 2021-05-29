from io import SEEK_CUR
from re import S
import networkx as nx
import numpy as np
from classes.node import Node


class Graph:

    def __init__(self, board):
        self.__graph = np.zeros(
            (board.size, board.size), dtype=np.object)

    # initialize nodes values (1-9) from board
    def init_nodes(self, board):
        for row in range(board.size):
            for col in range(board.size):
                node = Node((row, col), board.board_at((row, col)))
                self.__graph[row][col] = node

    # set adjacent nodes for every node
    def set_adj_nodes(self, board):
        #MAYBE CHANGE TO A DICT OF DICT INSTEAD OF DICT OF LISTS
        nodes_per_col={}
        nodes_per_line={}
        nodes_per_block={}

        for i in range(board.size):
            nodes_per_col[i]=list()
            nodes_per_line[i]=list()
            nodes_per_block[i]=list()
        
        #fill in all dicts
        for row in range(board.size):
            for col in range(board.size):  
                nodes_per_line[row].append(self.__graph[row][col])
                nodes_per_col[col].append(self.__graph[row][col])
                
                #get which block node is in
                block = max(int(row/3),int(col/3))
                nodes_per_block[block].append(self.__graph[row][col])
        
        #set row and col neighbours of each node
        for row in range(board.size):
            for col in range(board.size):
                
                #add all neighbours from its row
                for node in nodes_per_line[row]:
                    #make sure is not adding itself as neighbour
                    if node is not self.__graph[row][col]:
                        self.__graph[row][col].add_neighbour(node)
                
                #add all neighbours from its column
                for node in nodes_per_col[col]:
                    #make sure is not adding itself as neighbour
                    if node is not self.__graph[row][col]:
                        self.__graph[row][col].add_neighbour(node)

                block = max(int(row/3),int(col/3))

                #MAYBE CHANGE TO A DICT OF DICT INSTEAD OF DICT OF LISTS
                #add remaining nodes from the block
                for node in nodes_per_block[block]:
                    if node not in nodes_per_line[row] and node not in nodes_per_col[col]:
                        self.__graph[row][col].add_neighbour(node)



    def sudoku_solver(self, board):
        pass

    @property
    def graph(self):
        return self.__graph
