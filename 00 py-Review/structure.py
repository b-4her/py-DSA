
def main():
    print("Hello, World!")

    n1 = Node(1)
    n2 = Node(2, n1)
    print(n2.next.val)

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    main()