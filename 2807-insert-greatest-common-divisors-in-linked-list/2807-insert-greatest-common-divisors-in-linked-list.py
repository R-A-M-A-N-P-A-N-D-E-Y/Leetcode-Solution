# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        tmp = head
        while tmp.next:
            new = ListNode(gcd(tmp.val, tmp.next.val))
            new.next = tmp.next
            tmp.next = new
            tmp = new.next
        return head