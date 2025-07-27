# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
def reverseList(head):
  arr = []

  while head is not None:
    arr.append(head.data)
    head = head.next
  
  arr.sort()
  reversed_arr = arr[::-1]

  dummy = Node(-1)
  curr = dummy

  for value in reversed_arr:
    curr.next = Node(value)
    curr = curr.next
  
  return dummy.next
  
def printList(curr):
  while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  res = reverseList(head)
  printList(res)
# head = [1,2,3,4,5]
# output = [5,4,3,2,1]

# head = [1,2]
# output = [2,1]

# head = []
# output = []