class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def print_inorder(self):
        # inner sub function.
        def _print_inorder(cur_node):  # recursive, O(n) time, O(n) space (aux space)
            if cur_node.left:
                _print_inorder(cur_node.left)
            
            print(cur_node.val, end=" ")

            if cur_node.right:
                _print_inorder(cur_node.right)

        # call the inner recursive func
        _print_inorder(cur_node=self.root)
        print()

    def add(self, val_list, direction_list):
        cur = self.root
        for idx, direction in enumerate(direction_list):
            if direction == 'L':
                if cur.left:
                    assert cur.left.val == val_list[idx]
                else:
                    cur.left = Node(val_list[idx])
                cur = cur.left
            else:  # 'R'
                if cur.right: # if has right, check that the value is consistent with our expectations
                    assert cur.right.val == val_list[idx]
                else:
                    cur.right = Node(val_list[idx])
                cur = cur.right

    def level_order_traversal2(self):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(self.root)
        level = 0

        while nodes_queue:
            print(f'\nLevel {level}: ', end='')
            sz = len(nodes_queue)
            for _ in range(sz):
                cur = nodes_queue.popleft()
                print(cur.val, end=' ')

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)
                
            level += 1

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    tree.print_inorder()
    # 7 4 8 2 5 9 1 3 10 6
    tree.level_order_traversal2()



