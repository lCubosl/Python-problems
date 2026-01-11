# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10
        
            print(f"{v1} + {v2} = {total} → digit {digit}, carry {carry}")

            curr.next = ListNode(digit)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def reverse_number(arr):
    return int("".join(map(str, arr[::-1])))

l1_arr = [2, 4, 3]
l2_arr = [5, 6, 4]

l1 = build_list(l1_arr)
l2 = build_list(l2_arr)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
output_arr = list_to_array(result)

print("\nInput: l1 =", l1_arr, ", l2 =", l2_arr)
print("Output:", output_arr)