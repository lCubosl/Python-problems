from collections import deque

def build_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

class Solutio2(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

# Example input
tree_input = [1, None, 2, 3]

# Build tree
root = build_tree(tree_input)

# Run recursive solution
sol1 = Solution()
print("Input:", tree_input)
print("Recursive Inorder Output:", sol1.inorderTraversal(root))

# Run iterative solution
sol2 = Solutio2()
print("Iterative Inorder Output:", sol2.inorderTraversal(root))
