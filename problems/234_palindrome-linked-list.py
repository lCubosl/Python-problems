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

def isPalindrome(head):
  nums = []

  while head:
    nums.append(head.val)
    head = head.next
  
  l,r = 0, len(nums) - 1
  while l <= r:
    if nums[l] != nums[r]:
      return False
    l += 1
    r -= 1
  return True

if __name__ == "__main__":
  head = Node(1, Node(2, Node(2, Node(2))))

  print("Original list:")
  printList(head)

  result = isPalindrome(head)
  print(result)