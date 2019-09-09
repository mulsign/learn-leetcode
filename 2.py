# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        while(l1 and l2):
            r = l1.val + l2.val
            if(r < 10):
                ans.val = r
                ans.next = self.addTwoNumbers(l1.next, l2.next)
                return ans
            else:
                ans.val = r - 10
                l1.next = self.addTwoNumbers(l1.next,ListNode(1))
                ans.next = self.addTwoNumbers(l1.next, l2.next)
                return ans
        if(l1):
            return l1
        if(l2):
            return l2
            
x = ListNode(2)
x.next = ListNode(1)
y = ListNode(2)
y.next = ListNode(1)

so = Solution()
ans = so.addTwoNumbers(x,y)
print(ans.next.val)