class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

class BST:
    def __init__(self, val):
        self.root = Node(val)

    def search(self, val):
        def _search(cur, val):
            if not cur: # base case
                return False
            
            if cur.val > val:
                return _search(cur.left, val)
            elif cur.val < val:
                return _search(cur.right, val)
            
            return True  # equal (found)

        return _search(self.root, val)

    def insert(self, val):  # handle both single input and list search
        def _insert(cur, val):
            if cur.val == val:
                return  # don't insert anything
            
            if cur.val > val: # go to left
                if cur.left:
                    _insert(cur.left, val)
                else: # has no left
                    cur.left = Node(val)
            else: # go to right
                if cur.right:
                    _insert(cur.right, val)
                else:
                    cur.right = Node(val)

        if not isinstance(val, list):
            val = [val]
        for idx in range(len(val)):
            _insert(self.root, val[idx])

    def inorder(self):
        lst = []
        def _inorder(cur, lst):
            if not cur:
                return
            
            _inorder(cur.left, lst)
            lst.append(cur.val)
            _inorder(cur.right, lst)

        return _inorder(self.root, lst)

    def is_valid_bst(self):
        # check if all sorted
        lst = self.inorder()

        for idx in range(len(lst)-1):
            if lst[idx] >= lst[idx+1]: # = since duplicates are not allowed
                return False
            
        return True
    

    ############ DELETION 

    @staticmethod # utility function
    def get_min_val(cur: Node) -> int: # O(h) time
        min = 0
        while cur:
            min = cur.val
            cur = cur.left
        return min
        
    def delete(self, val):
        def _delete(cur: Node, val) -> Node:   # returns a pointer to the head
            if not cur:
                return None
            elif cur.val > val:
                cur.left = _delete(cur.left, val)
            elif cur.val < val:
                cur.right = _delete(cur.right, val)
            else: # found
                if cur.is_leaf():
                    return None
                elif not cur.right:
                    return cur.left # new head
                elif not cur.left:
                    return cur.right
                else: # both children exist (find successor)
                    min = BST.get_min_val(cur.right)
                    cur.val = min
                    cur.right = _delete(cur.right, min)  
                    # I noticed that successor here, can be either the min in the right
                    # or the max in the left, both should work fine in terms of deletion.
                    
                    # successor   = minimum value in right subtree الخلف او الوريث
                    # predecessor = maximum value in left subtree السلف
                    # (BOTH WORK)
            return cur
        
        self.root = _delete(self.root, val)

    ############ SUCCESSOR
    # if we have right sub tree, then the successor is the min of the right subtree
    
    # otherwise: keep going up until you find the first node that you are not on its right
    # if you don't find it then you are the max! no successor.

    # O(h) solution!

    # :) pretty simple  -- just imagine that you are in an order recursive order traversal.

    # TODO
    def find_chain(self, val):
        def _find_chain(val: int, cur: Node, lst: list) -> bool:
            if not cur:
                return False
            
            lst.append(cur)

            if cur.val < val:
                return _find_chain(val, cur.right, lst)
            elif cur.val > val:
                return _find_chain(val, cur.left, lst)
            else:
                return True

        lst = []
        found = _find_chain(val, self.root, lst)

        if not found:
            lst = []
        return lst
    
    # O(h) time
    def successor(self, val: int) -> int:  
    # returns None if not found, or val is max
        ancestors = self.find_chain(val)
        if not ancestors:
            return None # not found
        
        child = ancestors.pop()
        if child.right: # has right
            return BST.get_min_val(child.right)
        
        # no right:
        parent = ancestors.pop()
        while parent and parent.right == child:
            child = parent
            parent = None if not ancestors else ancestors.pop()

        if parent:
            return parent.val
        else:
            return None  # max


def test1():
    lst = [20, 70, 15, 45, 60, 73, 35]

    for val in lst:
        tree = BST(50)
        tree.insert(lst)

        tree.delete(val)
        assert not tree.search(val)

    print("SUCCESS 1")


def test2():
    lst = [20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58]

    for val in lst:
        tree = BST(50)
        tree.insert(lst)

        tree.delete(val)
        assert not tree.search(val)

    print("SUCCESS 2")


# testing deletion and successor
if __name__ == '__main__':
    test1()
    test2()

    tree = BST(50)
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