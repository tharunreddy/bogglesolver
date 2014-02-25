__author__ = 'Tharun'

from BoggleBoard import BoggleBoard
from Trie import Trie


class BoggleSolver:
    def __init__(self, board, trie):
        self._board = board
        self._wordsTrie = trie

    def solve(self):
        for pos in self._board.get_all_positions():
            self._solver(pos, [])

    def _solver(self, currentPos, posVisited):
        word_till_now = "".join(map(lambda pos: self._board.get(pos)[0], posVisited))
        current_word = word_till_now + self._board.get(currentPos)[0]
        if self._wordsTrie.get(current_word):
            print current_word
        elif len(current_word) < 4:
            pass
        else:
            return
        for pos in self._board.get_successors(currentPos):
            if pos not in posVisited:
                positions = posVisited[:]
                positions.append(currentPos)
                self._solver(pos, positions)

def main():
    from string import ascii_lowercase
    from random import choice
    import csv, re
    b = BoggleBoard()
    for i in range(4):
        for j in range(4):
            b.put((i,j), choice(ascii_lowercase))
    t = Trie()
    words =[]
    with open("wordsList.csv", 'r') as f:
        wl = csv.reader(f)
        for l in wl:
            words.extend(l)
    for word in words:
        if re.match(r"^[a-z]*$", word):
            t.put(word, len(word))

    solver = BoggleSolver(b, t)
    solver.solve()

if __name__ == "__main__":
    main()