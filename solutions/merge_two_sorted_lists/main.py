class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(None)
        i = prehead
        while True:
            if l1 is None and l2 is None:
                return prehead.next
            elif l1 == None:
                i.next = l2
                return prehead.next
            elif l2 == None:
                i.next = l1
                return prehead.next
            elif l1.val <= l2.val:
                i.next = l1
                i = i.next
                l1 = l1.next
            else:
                i.next = l2
                i = i.next
                l2 = l2.next
