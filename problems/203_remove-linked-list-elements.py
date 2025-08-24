# Definition for singly-linked list.
class Node(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def printList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")

def removeElements(head, val):
  dummy = Node(0)
  dummy.next = head
  current = dummy

  while current.next:
    if current.next.val == val:
      current.next = current.next.next
    else:
      current = current.next

  return dummy.next

if __name__ == "__main__":
  # Create list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
  head = Node(1, Node(2, Node(6, Node(3, Node(4, Node(5, Node(6)))))))

  print("Original list:")
  printList(head)

  new_head = removeElements(head, 6)

  print("After removing 6:")
  printList(new_head)