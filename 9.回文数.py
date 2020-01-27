#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.66%)
# Likes:    852
# Dislikes: 0
# Total Accepted:    219.2K
# Total Submissions: 386.2K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#


# class Solution2:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         rev = 0
#         ori = x
#         while x:
#             rev = rev*10 + x%10
#             x = x // 10
#         if ori == rev:
#             return True
#         else:
#             return False 


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        while len(l) >= 2:
            if l.pop(-1) != l.pop(0):
                return False
        return True
# @lc code=end