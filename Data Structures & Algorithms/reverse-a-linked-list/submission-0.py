# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [val,next] ----> [val,next] ----> [val,none]

#salva il next di next
#aggiorna il successivo di next con me
#aggiorna il curr con next
#aggiorna il mio next col precedente 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        return prev
