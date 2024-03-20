# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        i = 0
        while temp:
            if i == a-1:
                tempa = temp
            elif i == b+1:
                tempb = temp
            i += 1
            temp = temp.next
        
        temp = list2
        while temp.next:
            temp = temp.next

        tempa.next = list2
        temp.next = tempb

        return list1