

class Node():

    def __init__(self, pos, color):
        self.__color = color
        self.__pos = pos
        self.__neighbours = {}

    @property
    def color(self):
        return self.__color
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def neighbours(self):
        return self.__neighbours
    
    def add_neighbour(self, node):
        self.__neighbours[node.pos]=node