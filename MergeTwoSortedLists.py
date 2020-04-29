
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printAllNode(self):
        tracer = self
        while(tracer.next != None):
            print(tracer.val)
            tracer = tracer.next
        print(tracer.val)

class Solution:
    def mergeTwoLists(self, l1, l2):
        tracer = output = ListNode(0)
        while(l1 or l2):
            if(l1 == None):
                tracer.next = l2
                l2 = l2.next
                tracer = tracer.next

            elif (l2 == None):
                tracer.next = l1
                l1 = l1.next
                tracer = tracer.next

            elif(l1.val < l2.val):
                tracer.next = l1
                l1 = l1.next
                tracer = tracer.next
            else:
                tracer.next = l2
                l2 = l2.next
                tracer = tracer.next
        return output.next


