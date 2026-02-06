# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        return dummy.next

# Helper: build linked list from Python list
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper: print linked list nicely
def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) if values else "[]")

s = Solution()

head = build_list([1, 2, 3, 4])
print("Input:")
print_list(head)

new_head = s.swapPairs(head)
print("Output:")
print_list(new_head)
