class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        i = head
        while i is not None:
            temp = i.next
            i.next = new_head
            new_head = i
            i = temp
        return new_head
