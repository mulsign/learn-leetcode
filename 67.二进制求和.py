#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (51.14%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    58.5K
# Total Submissions: 112.7K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
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
      
        
# @lc code=end

