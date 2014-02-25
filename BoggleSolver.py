__author__ = 'Tharun'

from BoggleBoard import BoggleBoard
from Trie import Trie


class BoggleSolver:
    def __init__(self, board, trie):
        self._board = board
        self._wordsTrie = trie

    def solve(self):
        for pos in self._board.get_all_positions():
            self._solver(pos)

    def _solver(self, startingPos):
    def get_words(self):
        pass
