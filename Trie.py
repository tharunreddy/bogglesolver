__author__ = 'Tharun'

import string
import csv
import re


class Trie:
    """
    This class implements the Trie Data Structure.
    """

    class Node:
        """
        Inner class Node, R way tree where R is the alphabets in english (lowercase)
        """
        def __init__(self):
            self.value = None
            self.next = {k: None for k in string.ascii_lowercase}

    def __init__(self):
        self._root = None

    def _get(self, root, key, d):
        if root is None:
            return None
        if d is len(key):
            return root
        char = key[d]
        return self._get(root.next[char], key, d+1)

    def get(self, key):
        """
        Takes a string and returns a value
        key   a string whose value you would like to get
        """
        node = self._get(self._root, key, 0)
        if node is None: return None
        return node.value

    def _put(self, root, key, value, d):
        if root == None:
            root = self.Node()
        if d == len(key):
            root.value = value
            return root
        char = key[d]
        try:
            root.next[char] = self._put(root.next[char], key, value, d+1)
        except KeyError:
            print "There was a key error", key
            return root
        return root

    def put(self, key, value):
        """
        Puts the value corresponding to the given key here.
        """
        self._root = self._put(self._root, key, value, 0)



def test_wordList():
    """
    This method tests the trie above
    """

    t = Trie()
    words =[]
    with open("wordsList.csv", 'r') as f:
        wl = csv.reader(f)
        for l in wl:
            words.extend(l)



    for word in words:
        if re.match(r"^[a-z]*$", word):
            t.put(word, len(word))




from itertools import product
import cProfile
def main():
    cProfile.run("test_wordList()")


if __name__ == "__main__":
    main()