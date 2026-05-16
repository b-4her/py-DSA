class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    process(current.left, val)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    process(current.right, val)
            # Elise - already exists

        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)

    def inorder(self, current):
        def process(current):
            if not current:
                return
            process(current.left)
            lst.append(current.val)
            process(current.right)

        lst = []
        process(current)
        return lst

    # the inorder traversal must be: 1) sorted 2) unique (no duplicates)
    def isValidBST(self, current):
        lst = self.inorder(current)
        # We can do the comparison without loop
        for idx in range(1, len(lst)):
            if lst[idx-1] >= lst[idx]:
                return False
        return True

    def search(self, val):
        def _search(current, val):
            if not current:
                return False

            if current.val == val:
                return True

            if val < current.val:
                return _search(current.left, val)

            _search(current.right, val)

        return _search(self.root, val)

    ##################################

    def min_node(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur

    def delete(self, val):
        def process(current, val):
            if not current:
                return

            if val <  current.val:  # Value on the left side
                # the left subtree will be changed. This can be left itself
                current.left = process(current.left, val)   # must link
                return current

            if val >  current.val:  # Value on the right side
                current.right = process(current.right, val)
                return current

            # we found the node: we have 3 cases
            if current.is_leaf():   # case 1: leaf
                return None         # Just remove

            if not current.right:      # case 2: has left only
                current = current.left
                return current

            if not current.left:      # case 2: has right only
                current = current.right
                return current

            # 2 children: Use successor
            mn = self.min_node(current.right)
            current.val = mn.val    # copy data
            current.right = process(current.right, mn.val)
            return current

        process(self.root, val)


def test1():
    lst = [20, 70, 15, 45, 60, 73, 35]

    for val in lst:
        tree = BinaryTree(50)
        tree.insert(lst)

        tree.delete(val)
        assert not tree.search(val)


def test2():
    lst = [20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58]

    for val in lst:
        tree = BinaryTree(50)
        tree.insert(lst)

        tree.delete(val)
        assert not tree.search(val)


if __name__ == '__main__':
    test1()
    test2()
