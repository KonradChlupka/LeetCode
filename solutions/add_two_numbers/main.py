class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l1_start = l1
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            l1.val = out
            if not l1.next and (carry or (l2 and l2.next)):
                l1.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next if l2 else None
        return l1_start
