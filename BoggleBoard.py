__author__ = 'Tharun'

"""
A implementation of the Board for Boggle
"""

from itertools import product
import copy


class BoggleBoard:

    def __init__(self, n=4):
        self._n = n
        self._board = [list([None]*self._n) for i in range(self._n)]
        #self._board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def get(self, pos):
        """
        Returns the character at (i, j) of the board
        pos (i,j) where i and j are between(0, n) inclusive
        """
        try:
            i, j = pos
        except ValueError:
            print "Your position parameter should be (i, j)"
            return None
        return (self._board[i][j], i*self._n + j)

    def put(self, pos, value):
        """
        Inserts the value at the particular position indicated by pos
        pos is (i, j)
        """
        try:
            i,j = pos
        except ValueError:
            print "Your position parameter should be (i, j)"
            return None
        self._board[i][j] = value
        return True

    def get_successors(self, pos):
        """
        Returns the successors i.e. surrounding cells for the given position
        """
        successors = []
        try:
            i, j = pos
        except ValueError:
            print "Your position parameter should be (i, j)"
            return None
        for position in product((i-1, i, i+1), (j-1, j, j+1)):
            x, y = position
            if x in range(0, self._n) and y in range(0, self._n) and pos != position:
                successors.append(position)
        return map(self.get, successors)

    def print_board(self):
        for i in range(self._n):
            line = " | "
            print "-"*5*self._n
            for j in range(self._n):
                line += self.get((i,j))[0]
                line += " | "
            print line
        print "-"*5*self._n

    def get_all_positions(self):
        return [(i, j) for i in range(self._n) for j in range(self._n)]


def main():
    """
    Test class for boggle board
    """
    from string import ascii_lowercase
    from random import choice
    b = BoggleBoard()
    for i in range(4):
        for j in range(4):
            b.put((i,j), choice(ascii_lowercase))
    b.print_board()
    print b.get_all_positions()
    #print b.get_successors((3,2))

if __name__ == "__main__":
    main()
