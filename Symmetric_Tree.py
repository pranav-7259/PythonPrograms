#Using stacks

import collections
from unittest.mock import NonCallableMagicMock
from urllib.parse import non_hierarchical
class Solution:
    def isSymmetric_DFS(self, root):
        if root is None:
            return True
       
        stack = [(root.left, root.right)]
        while len(stack) > 0:
            left, right = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        
        return True