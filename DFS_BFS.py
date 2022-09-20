from collections import deque


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_Child(self, data):

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_Child(data)
            else:
                self.left = BSTNode(data)

        if data > self.data:
            if self.right:
                self.right.add_Child(data)
            else:
                self.right = BSTNode(data)

    def dfs(self):

        dfs_list = []
        if self.left:
            dfs_list += self.left.dfs()

        dfs_list.append(self.data)

        if self.right:
            dfs_list += self.right.dfs()

        return dfs_list

    def bfs(self):

        q = deque()
        q.appendleft(self)
        bfs_list = []

        while len(q) > 0:

            if q[-1].left:
                q.appendleft(q[-1].left)

            if q[-1].right:
                q.appendleft(q[-1].right)

            element = q.pop()
            bfs_list.append(element.data)

        return bfs_list


def build_tree(elements):
    root = BSTNode(elements[0])
    for i in range(1, len(elements)):
        root.add_Child(elements[i])

    return root


if __name__ == '__main__':
    elements = [50, 30, 20, 40, 70, 60, 80]
    tree = build_tree(elements)
    print(tree.dfs())
    print(tree.bfs())

    #  BST
    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80
