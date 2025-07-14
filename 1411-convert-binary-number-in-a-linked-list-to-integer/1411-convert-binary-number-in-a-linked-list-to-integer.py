# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        arr = []
        l = 1
        temp = head
        while temp.next:
            l += 1
            arr.append(temp.val)
            temp = temp.next
        arr.append(temp.val)

        for i in range(l):
            # print(arr[i])
            if arr[i] == 1:
                res += 2 ** (l - i - 1)
        
        return res