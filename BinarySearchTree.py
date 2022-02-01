COUNT = [10]


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    class Node:
        def __init__(self, val):
            self.leftChild = None
            self.rightChild = None
            self.value = val

    def insert(self, val):
        new_node = self.Node(val)
        if self.root is None:  # if tree is empty set new_node as root
            self.root = new_node
            return

        curr = self.root
        while True:
            if val > curr.value:
                if curr.rightChild is None:
                    curr.rightChild = new_node
                    return
                else:
                    curr = curr.rightChild
            else:
                if curr.leftChild is None:
                    curr.leftChild = new_node
                    return
                else:
                    curr = curr.leftChild

    # Wrapper over print2DUtil()
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
            print(root.value)

            # Process left child
            print2DUtil(root.leftChild, space)

        # space=[0]
        # Pass initial space count as 0 / pass root
        print2DUtil(self.root, 0)

    def getTotalHeight(self):

        def nodeHeight(root):
            if root is None:
                return -1
            return max(nodeHeight(root.leftChild), nodeHeight(root.rightChild)) + 1

        def totalHeight(root):
            if root is None:
                return 0
            return totalHeight(root.leftChild) + nodeHeight(root) + totalHeight(root.rightChild)

        return totalHeight(self.root)

    def getWeightBalanceFactor(self):

        def balanceFactor(root):
            if root is None:
                return 0
            left = balanceFactor(root.leftChild)
            right = balanceFactor(root.rightChild)
            return max(abs(left - right), abs(right - left)) + 1

        return balanceFactor(self.root)


if __name__ == "__main__":
    x = BST()
    x.insert(6)
    x.insert(4)
    x.insert(9)
    x.insert(5)
    x.insert(8)
    x.insert(7)
    # x.insert(3)
    # # x.insert(4)
    # # x.insert(2)
    # x.insert(7)
    # x.insert(1)
    # x.insert(5)
    # x.insert(12)
    # x.insert(15)
    # x.insert(18)

    x.printer()
    print("\n" + "total height")
    print(x.getTotalHeight())
    print(x.getWeightBalanceFactor())
