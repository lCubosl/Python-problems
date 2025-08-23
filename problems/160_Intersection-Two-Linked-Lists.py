class Node(object):
   def __init__(self, data):
      self.data = data
      self.next = None

def printList(head):
  current = head
  while current:
    print(current.data, end=" -> ")
    current = current.next
  print("None")
  
def getIntersectionNode(headA, headB):
  l1, l2 = headA, headB
  while l1 != l2:
    l1 = l1.next if l1 else headB
    l2 = l2.next if l2 else headA
  return l1

# Example usage
if __name__ == "__main__":
    # Create common intersection part
    common = Node(30)
    common.next = Node(40)
    common.next.next = Node(50)

    # Create first list: 10 -> 20 -> 30 -> 40 -> 50
    headA = Node(10)
    headA.next = Node(20)
    headA.next.next = common

    # Create second list: 15 -> 30 -> 40 -> 50
    headB = Node(15)
    headB.next = common

    # Print both lists
    print("List A:")
    printList(headA)
    print("List B:")
    printList(headB)

    # Find intersection
    intersection = getIntersectionNode(headA, headB)
    if intersection:
        print(f"Intersection at node with data = {intersection.data}")
    else:
        print("No intersection found.")