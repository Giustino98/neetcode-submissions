class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr is not None:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr =  tmp_next
        return prev