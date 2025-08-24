# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def printList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")

def isPalindrome(self, head):
  pass