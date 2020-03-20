#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
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
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        re = ans
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum // 10
            re.next = ListNode(sum % 10)
            re = re.next
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        if carry > 0:
            re.next = ListNode(1)
        return ans.next

