
from MergeTwoSortedLists import Solution
from MergeTwoSortedLists import ListNode


l1 = ListNode(0)
l1.next = ListNode(1)
l1.next.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(5)

a = Solution()

a.mergeTwoLists(l1, l2).printAllNode()
