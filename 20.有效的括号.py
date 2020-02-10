#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.91%)
# Likes:    1370
# Dislikes: 0
# Total Accepted:    197.9K
# Total Submissions: 485.5K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def match(self, a,b) -> bool:
        return (a == "(" and b == ")") or (a == "[" and b == "]") or (a == "{" and b == "}")
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
            if i in [")","]","}"]:
                if len(stack) == 0 or not self.match(stack[-1],i):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0



# @lc code=end

