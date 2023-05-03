# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        if head.next:
            curr1 = curr2 = head
            values.append(head.val)
            length = 1
            while curr2.next:
                curr2 = curr2.next
                values.append(curr2.val)
                length += 1

            curr3 = curr2
            values.pop()
            while values:
                curr2.next = ListNode(values.pop())
                curr2 = curr2.next

            cnt = 1
            flag = True
            while cnt <= length//2:
                if curr1.val == curr3.val:
                    curr1 = curr1.next
                    curr3 = curr3.next
                    cnt += 1
                else:
                    flag = False
                    break
            return flag
        else:
            return True