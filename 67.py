class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
        
class Solution:
    def str2lt(self, s: str) -> ListNode:
        lt = ListNode(0)
        while(len(s)):
            if(s[-1] == '1'):
                lt.val = 1
                print('1')
            else:
                lt.val = 0
                print('0')
            print(s[:-1])
            lt.next = self.str2lt(s[:-1])
            return lt
        return lt.next
    
    def lt2str(self, lt: ListNode) -> str:
        s = ''
        while(lt):
            s = str(lt.val) + s
            lt = lt.next
        return s
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        while(l1 and l2):
            r = l1.val + l2.val
            if(r < 2):
                ans.val = r
                ans.next = self.addTwoNumbers(l1.next, l2.next)
                return ans
            else:
                ans.val = r - 2
                l1.next = self.addTwoNumbers(l1.next,ListNode(1))
                ans.next = self.addTwoNumbers(l1.next, l2.next)
                return ans
        if(l1):
            return l1
        if(l2):
            return l2
            
    def addBinary(self, a: str, b: str) -> str:
        lta = self.str2lt(a)
        ltb = self.str2lt(b)
        ans = self.addTwoNumbers(lta,ltb)
        return(self.lt2str(ans))
      