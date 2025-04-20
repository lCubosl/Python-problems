# 173. Binary Search Tree Iterator
# helper funtion to write the tree
class TreeNode():
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def build_tree(values):
  if not values:
      return None

  root = TreeNode(values[0])
  queue = [root]
  i = 1

  while i < len(values):
      current = queue.pop(0)

      if i < len(values) and values[i] is not None:
          current.left = TreeNode(values[i])
          queue.append(current.left)
      i += 1

      if i < len(values) and values[i] is not None:
          current.right = TreeNode(values[i])
          queue.append(current.right)
      i += 1
  return root

# Solution: iterator thorugh tree
class BSTIterator():
  def __init__(self, root):
    self.stack = []

    while root:
      self.stack.append(root)
      root = root.left

  def next(self):
    res = self.stack.pop()
    cur = res.right
    while cur:
      self.stack.append(cur)
      cur = cur.left

    return res.val

  def hasNext(self):
    return self.stack != []
  

tree = build_tree([7, 3, 15, None, None, 9, 20])

bSTIterator = BSTIterator(tree)
print(bSTIterator.next())
print(bSTIterator.next())    
print(bSTIterator.hasNext()) 
print(bSTIterator.next())    
print(bSTIterator.hasNext()) 
print(bSTIterator.next())    
print(bSTIterator.hasNext()) 
print(bSTIterator.next())    
print(bSTIterator.hasNext()) 
