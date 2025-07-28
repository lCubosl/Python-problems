# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None    
    
def hasCycle(head):
  s, f = head, head

  while f and f.next:
    s = s.next
    f = f.next.next
    if s == f:
      return True

  return False
  
def printList(curr):
  while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next

if __name__ == "__main__":
  head = Node(3)
  head.next = Node(2)
  head.next.next = Node(0)
  head.next.next.next = Node(-4)

  res = hasCycle(head)
  printList(res)
