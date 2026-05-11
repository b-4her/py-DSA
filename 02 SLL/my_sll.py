def main():
    print("Hello World!")
    lst = LinkedList()
    lst.print_list()

    lst.add_first(1)
    lst.add_first(2)
    lst.add_first(3)
    lst.print_list() # 3 2 1

    lst.add_last(0) # 3 2 1 0
    lst.print_list()

    lst.add(0, -1)
    lst.add(6, -2)
    lst.add(1, -3)
    lst.add(1, -4)
    lst.print_list()


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, val):
        new_node = Node(val)

        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def add_first(self, val):
        new_node = Node(val)

        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add(self, idx, val): 
        new_node = Node(val)
    
        prev = None 
        cur = self.head
        while(idx != 0 and cur!= None):
            prev = cur
            cur = cur.next
            idx = idx-1

        if not prev:
            self.add_first(val)
        elif not cur:
            self.add_last(val)
        else:
            prev.next = new_node
            new_node.next = cur

    # def remove(self, idx=0):  # later
    #     ...

    # def reverse(self):  # later
    #     ...

    def print_list(self):
        cur = self.head
        if (not cur):
            print("List is still empty!")
            return

        while (cur):
            print(cur.val, end=" ")
            cur = cur.next
        print()
    

if __name__ == "__main__":
    main()