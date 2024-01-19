class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def traverse_tree(node):
    if node is not None:
        print(node.value)
        traverse_tree(node.left)
        traverse_tree(node.right)


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5


    """

    1
   / \
  2   3
 / \
4   5

"""

    traverse_tree(node1)


if __name__ == "__main__":
    main()
