class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data


def calculate_sum(root):
    if root is None:
        return 0
    return root.data + calculate_sum(root.left) + calculate_sum(root.right)


def build_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])

    for i in range(1, len(numbers)):
        root.add_child(numbers[i])

    return root


if __name__ == '__main__':
    numbers = [10, 3, 5, 1, 45, 67, 89, 100]
    tree = build_tree(numbers)
    print(tree.find_min())
    print(tree.find_max())
    print(sum(numbers), calculate_sum(tree))
