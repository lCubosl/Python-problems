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

# 1st solution: 
# 1. convert each value of the linked list to an item in the dictionary
# 2. left right pointer each value of the dictionary
# 3. compare values. If every value matches, its a palindrome
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

# 1st solution: 
# 1. slow and fast pointer. fast moves twice as fast as slow. 
# 2. when fast reaches the end, slow  will reach the middle
# 3. reverse the 2nd half of the linked list through standard linked list reversal
# 4. compare halves. (l first half, r second half reversed list)
def isPalindromeAlt(head):
  fast = head
  slow = head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

  prev = None
  while slow:
    tmp = slow.next
    slow.next = prev
    prev =  slow
    slow = tmp

  l, r = head, prev
  while r:
    if l.val != r.val:
      return False
    l = l.next
    r = r.next
  return True

if __name__ == "__main__":
  head = Node(1, Node(2, Node(2, Node(2))))

  print("Original list:")
  printList(head)

  result1 = isPalindrome(head)
  print(result1)

  result2 = isPalindromeAlt(head)
  print(result2)