# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        arr = []
        if n < k:

            while head:
                temp = head
                head = head.next
                temp.next = None
                arr.append(temp)

            temp = ListNode()
            temp.next = None
            temp.val = ''

            for _ in range(k-n):
                arr.append(temp)

        else:
            num = n // k
            arr = [num] * k

            for i in range(n - (num*k)):
                arr[i] += 1
            
            for i in range(k):
                temp = head
                part_size = arr[i]
                prev = None  # To keep track of the previous node
                while part_size > 0 and temp:
                    prev = temp
                    temp = temp.next
                    part_size -= 1
                if prev:
                    prev.next = None  # Safely disconnect the end of the current part
                arr[i] = head  # Store the current head to the result list
                head = temp  # Move the head to the next part
                    
        return arr