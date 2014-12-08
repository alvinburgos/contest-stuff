import unittest
import random
from structs.avl import AVL, _h

def height(n):
    return 
def correct_height(n):
    if n is None:
        return True
    return correct_height(n.left) and correct_height(n.right) and max(_h(n.left), _h(n.right)) + 1 == n.height
def correct_avl(n):
    if n is None:
        return True
    return correct_avl(n.left) and correct_avl(n.right) and abs(_h(n.left) - _h(n.right)) < 2

class TestAVL(unittest.TestCase):
    def setUp(self):
        self.tree = AVL()
        arr = range(1000)
        random.shuffle(arr)
        for i in arr:
            self.tree.insert(i)
    def test_heights(self):
        self.assertTrue(correct_height(self.tree._root))
    def test_avl_prop(self):
        self.test_heights()
        self.assertTrue(correct_avl(self.tree._root))
