class Node(object):
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.height = 1
        self.count = 0
        self.val = val

def _h(n):
    if n is None:
        return 0
    return n.height

def _bal(n):
    return _h(n.right) - _h(n.left)

def _set_height(n):
    n.height = max(_h(n.left), _h(n.right)) + 1

def _rotate_right(n):
    child = n.left
    n.left = child.right
    child.right = n
    _set_height(child)
    _set_height(n)
    return n

def _rotate_left(n):
    child = n.right
    n.right = child.left
    child.left = n
    _set_height(child)
    _set_height(n)
    return n

def _insert(n, val):
    if n == None:
        return Node(val=val)
    if val == n.val:
        return n
    elif val < n.val:
        n.left = _insert(n.left, val)
        if _bal(n) == -2:
            if _h(n.left.left) < _h(n.left.right):
                n.left = _rotate_left(n.left)
            return _rotate_right(n, n.left)
    else:
        n.right = _insert(n.right, val)
        if _bal(n) == 2:
            if _h(n.right.right) < _h(n.right.left):
                n.right = _rotate_right(n.right)
            return _rotate_left(n)

def _find(n, val):
    if n == None:
        return False
    if val == n.val:
        return True
    elif val < n.val:
        return find(n.left, val)
    else:
        return find(n.right, val)


class AVL(object):
    def __init__(self):
        self._root = None
    def insert(self, val):
        self._root = _insert(self._root, val)
    def delete(self, val):
        pass
    def find(self, val):
        return _find(self._root, val)


