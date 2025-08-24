# Definition for singly-linked list.
class Node(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def printList(head):
  current = head
  while current:
    print(current.data, end=" -> ")
    current = current.next
  print("None")

def removeElements(head, val):
    """
    :type head: Optional[ListNode]
    :type val: int
    :rtype: Optional[ListNode]
    """
        