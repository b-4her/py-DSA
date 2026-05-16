# https://leetcode.com/problems/symmetric-tree/

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def min(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def find_chain(self, val):
        # return list of nodes on the path from root to value
        def process(current, val):
            if not current:
                return False

            self.lst.append(current)

            if val == current.val:
                return True
            if val < current.val:
                return process(current.left, val)
            return process(current.right, val)

        self.lst = []
        if process(self.root, val):
            return self.lst
        return None

    def successor(self, target):
        ancestors = self.find_chain(target)
        if not ancestors:   # value is not in tree!
            return None
        child = ancestors.pop()

        if child.right:
            return self.min(child.right)
        if not ancestors:   # root
            return None

        parent = ancestors.pop()
        # Cancel chain of ancestors I am BIGGER than them
        while parent and parent.right == child:
            child = parent
            parent = None if not ancestors else ancestors.pop()

        if not parent:
            return None
        return parent.val



if __name__ == '__main__':
    tree = BinaryTree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]
    tree.insert(lst)

    lst.append(50)
    lst.append(51)
    lst = sorted(lst)
    print(lst)

    for val in lst:
        print(val, tree.successor(val))

'''
[15, 20, 35, 45, 50, 51, 60, 70, 73]
15 20
20 35
35 45
45 50
50 60
51 None
60 70
70 73
73 None
'''