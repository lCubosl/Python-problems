class Node(object):
   def __init__(self, data):
      self.data = data
      self.next = None

def printList(self, headA, headB):
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