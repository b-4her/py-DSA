import inspect


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, initial_values=None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []  # add/remove nodes you use

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node does't exist!!")
            return

        self.length -= 1

    def debug_print_address(self):
        cur = self.head

        while cur is not None:
            print(f'{cur.data}@{id(cur)}', end='\t->\t')
            cur = cur.next
        print('None')

    def debug_print_node(self, node):
        if node is None:
            print('None')
            return

        prev_value = 'None' if node.prev is None else str(node.prev.data)
        print(prev_value.ljust(5), end='\t')

        print(str(node.data).ljust(5), end=' -> ')

        next_value = 'None' if node.next is None else str(node.next.data)
        print(next_value.ljust(5), end='\t')

        if node == self.head:
            print("head")
        elif node == self.tail:
            print("tail")
        else:
            print("")

    def debug_print_existing_nodes(self, msg=None):
        if msg:
            print(msg)

        for node in self.debug_data:
            self.debug_print_node(node)

        print('*******************')
        self.debug_verify_data_integrity()

    def debug_verify_data_integrity(self):
        if self.length == 0:
            assert self.head is None
            assert self.tail is None
            return

        assert self.head is not None
        assert self.head.prev is None
        assert self.tail is not None
        assert self.tail.next is None

        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            assert self.length == len(self.debug_data)

            # Verify forward pass
            actual_lst_len = 0
            cur = self.head

            while cur is not None:
                cur = cur.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len
            
            # Verify backward pass 
            actual_lst_len = 0
            cur = self.tail

            while cur is not None:
                cur = cur.prev
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len

    ##############################################
    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def insert_end(self, value):
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self._link(self.tail, node)
            self.tail = node

        self.debug_verify_data_integrity()  # ** verify as possible

    def print(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end='->')
            cur = cur.next
        print('None')

    def print_reversed(self):
        cur = self.tail

        while cur is not None:
            print(cur.data, end='->')
            cur = cur.prev
        print('None')

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

    def __repr__(self):
        represent = ''
        cur = self.head

        while cur is not None:
            represent += str(cur.data)
            cur = cur.next
            if cur:
                represent += ', '

        return represent
    ##############################################


def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([6, 10, 8, 15])
    lst.debug_print_existing_nodes()

    result = str(lst)
    expected = '6, 10, 8, 15'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    print('PASSED\n')


if __name__ == '__main__':
    test1()

    # Must see to insure no RTE
    print('ALL CASES PASSED')

