# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        curr = head
        prev = None

        while curr:
            ele = curr.val
            if ele in num_set:
                if prev:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    head = curr.next
                    curr = head
            else:
                prev = curr
                curr = curr.next
        
        return head