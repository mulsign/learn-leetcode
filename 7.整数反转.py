#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    
    MAX_VALUE = (1<<31)-1
    MIN_VALUE = -(1<<31)
    def reverse(self, x: int) -> int:
        res = 0
        y = abs(x)
        while y:
            res = res*10 + y%10
            if res > (self.MAX_VALUE if x > 0 else -self.MIN_VALUE):
                return 0
            y = y //10
        return res if x>0 else -res
# @lc code=end

