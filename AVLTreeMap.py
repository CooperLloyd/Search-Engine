COUNT = [10]


class AVL:
    def __init__(self):
        self.root = None
        self.size = 0

    class Node:
        def __init__(self, key, val):
            self.leftChild = None
            self.rightChild = None
            self.value = val
            self.height = 1
            self.key = key
            self.bf = 0

    def getHeight(self, node):
        def height(root):
            if root is None:
                return 0

            return max(height(root.leftChild), height(root.rightChild)) + 1
        return height(node)

    def get(self, key):

        def getVal(root):
            if root is None:
                return
            if root.key == key:
                return root.value
            elif key < root.key:
                return getVal(root.leftChild)
            elif key > root.key:
                return getVal(root.rightChild)
            else:
                return None

        return getVal(self.root)

    # rotate node right
    def rightRotate(self, node):
        # set up pointers
        pivot = node.left
        temp = pivot.right

        # execute rotation
        pivot.right = node
        node.left = temp

        # updating heights and balance factors
        node.height = self.getHeight(node)
        node.bf = self.getHeight(node.leftChild) - self.getHeight(node.rightChild)
        temp.height = self.getHeight(temp)
        temp.bf = self.getHeight(temp.leftChild) - self.getHeight(temp.rightChild)

    # rotate node left
    def leftRotate(self, node):
        # set up pointers
        pivot = node.right
        temp = pivot.left

        # execute rotation
        pivot.left = node
        node.right = temp

        # updating heights and balance factors
        node.height = self.getHeight(node)
        node.bf = self.getHeight(node.leftChild) - self.getHeight(node.rightChild)
        temp.height = self.getHeight(temp)
        temp.bf = self.getHeight(temp.leftChild) - self.getHeight(temp.rightChild)

    # returns rebalanced tree for all unbalanced cases
    def balance(self, node):
        if node.bf == 2:
            if node.leftChild.bf < 0:  # left-Right rotation
                self.rightRotate(node.right)
                self.leftRotate(node)
            else:
                self.rightRotate(node)  # left-left rotation
        elif node.bf == -2:
            if node.rightChild.bf > 0:  # right-left rotation
                self.rightRotate(node.rightChild)
                self.leftRotate(node)
            else:
                self.leftRotate(node)  # right-right rotation

    def insert(self, key, val):
        new_node = self.Node(key, val)
        if self.root is None:  # if tree is empty set new_node as root
            self.root = new_node
            return

        curr = self.root
        while True:
            if key > curr.key:
                if curr.rightChild is None:
                    curr.rightChild = new_node
                    break
                else:
                    curr = curr.rightChild
            else:
                if curr.leftChild is None:
                    curr.leftChild = new_node
                    break
                else:
                    curr = curr.leftChild

        # update node bf and height here
        new_node.height = self.getHeight(new_node)
        new_node.bf = self.getHeight(new_node.leftChild) - self.getHeight(new_node.rightChild)

        # balance tree with rotations
        self.balance(new_node)
    def printer(self):
        # Function to print binary tree in 2D
        # It does reverse inorder traversal
        def print2DUtil(root, space):

            # Base case
            if root is None:
                return

            # Increase distance between levels
            space += COUNT[0]

            # Process right child first
            print2DUtil(root.rightChild, space)

            # Print current node after space
            # count
            print()
            for i in range(COUNT[0], space):
                print(end=" ")
            print(root.key, "-", root.value)

            # Process left child
            print2DUtil(root.leftChild, space)

        # space=[0]
        # Pass initial space count as 0 / pass root
        print2DUtil(self.root, 0)


if __name__ == "__main__":
    x = AVL()
    x.insert(15, "bob")
    x.insert(20, "anna")
    x.insert(24, "tom")
    print(x.root.height)
    x.insert(10, "daivd")
    x.insert(13, "david")
    x.insert(7, "ben")
    x.insert(30, "karen")
    x.insert(36, "erin")
    x.insert(25, "david")
    x.insert(55, "erin")
    x.insert(66, "david")
    x.insert(64, "david")
    print(x.root.height)

    x.printer()

    # print(x.getHeight())
    # print(x.get(25))
