# Definition for singly-linked list.
# class Node
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# function delete duplicates with a set
def deleteDuplicates(head):
  arr = set()

  # add numbers to set
  while head is not None:
    arr.add(head.data)
    head = head.next
  
  # new dummy list with values. Set automatically removes the duplicates since
  # it can only have one of each value
  dummy = Node(-1)
  curr = dummy

  for value in arr:
    curr.next = Node(value)
    curr = curr.next
  
  return dummy.next

def printList(curr):
  while curr is not None:
    print(curr.data, end=" ")
    curr = curr.next
  print()

if __name__ == "__main__":
  # 1,1,2,3,3
  # 1,1,2
  head = Node(1)
  head.next = Node(3)
  head.next.next = Node(2)
  head.next.next.next = Node(2)

  res = deleteDuplicates(head)
  printList(res)