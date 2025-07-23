# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# function to merge two sorted lists
def mergeTwoLists(head1, head2):
  arr = []

  # list1 is apended to the array arr=[5,10,15]
  while head1 is not None:
    arr.append(head1.data)
    head1 = head1.next
  
  # list1 aleady in array. 
  # list2 is appended after arr=[5,10,15,2,3,20]
  while head2 is not None:
    arr.append(head2.data)
    head2 = head2.next
  
  # arr is sorted [2,3,5,10,15,20]
  arr.sort()

  # creates a new list with sorteed values
  dummy = Node(-1)
  curr = dummy

  for value in arr:
    curr.next = Node(value)
    curr = curr.next
  
  return dummy.next

# this function serves to print the liss
def printList(curr):
  while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next
  print()

if __name__ == "__main__":
  # the first linked list is 5 -> 10 -> 15
  head1 = Node(5)
  head1.next = Node(10)
  head1.next.next = Node(15)

  # the second linked list is 2 -> 3 -> 20
  head2 = Node(2)
  head2.next = Node(3)
  head2.next.next = Node(20)

  res = mergeTwoLists(head1, head2)

  # call to function mergeTwoLists. Prints result to console
  printList(res)