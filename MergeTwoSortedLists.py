
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printAllNode(self):
        tracer = self
        while(tracer.next != None):
            print(tracer.val)
            tracer = tracer.next
        print(print(tracer.val))


class Solution:
    def mergeTwoLists(self, l1, l2):
        tracer = output = ListNode(0)
        while(l1 and l2):
            print("l1:",l1.val,"l2:",l2.val)
            if(l1.val < l2.val):
                tracer.next = l1
                l1 = l1.next
            else:
                tracer.next = l2
                l2 = l2.next
            tracer = tracer.next
        return output.next


l1 = ListNode(0)
l1.next = ListNode(1)
l1.next.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(5)

a = Solution()

print(a.mergeTwoLists(l1, l2).printAllNode())
