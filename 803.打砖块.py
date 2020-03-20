#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#
# https://leetcode-cn.com/problems/bricks-falling-when-hit/description/
#
# algorithms
# Hard (21.90%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    451
# Total Submissions: 2K
# Testcase Example:  '[[1,0,0,0],[1,1,1,0]]\n[[1,0]]'
#
# 我们有一组包含1和0的网格；其中1表示砖块。 当且仅当一块砖直接连接到网格的顶部，或者它至少有一块相邻（4 个方向之一）砖块不会掉落时，它才不会落下。
# 
# 我们会依次消除一些砖块。每当我们消除 (i, j) 位置时， 对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这个消除而落下。
# 
# 返回一个数组表示每次消除操作对应落下的砖块数目。
# 
# 示例 1：
# 输入：
# grid = [[1,0,0,0],[1,1,1,0]]
# hits = [[1,0]]
# 输出: [2]
# 解释: 
# 如果我们消除(1, 0)位置的砖块, 在(1, 1) 和(1, 2) 的砖块会落下。所以我们应该返回2。
# 
# 示例 2：
# 输入：
# grid = [[1,0,0,0],[1,1,0,0]]
# hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：
# 当我们消除(1, 0)的砖块时，(1, 1)的砖块已经由于上一步消除而消失了。所以每次消除操作不会造成砖块落下。注意(1, 0)砖块不会记作落下的砖块。
# 
# 注意:
# 
# 
# 网格的行数和列数的范围是[1, 200]。
# 消除的数字不会超过网格的区域。
# 可以保证每次的消除都不相同，并且位于网格的内部。
# 一个消除的位置可能没有砖块，如果这样的话，就不会有砖块落下。
# 
# 
#

# @lc code=start

class WeightQU:
    def __init__(self, N: int):
        self.count = N
        self.id = []
        self.size = [1]*N
        for i in range(N):
            self.id.append(i)
    
    def find(self, p: int):
        while(p != self.id[p]):
            p = self.id[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)
    
    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        if(i == j):
            return
        if(self.size[i]<self.size[j]):
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
    
    def number(self):
        return self.size[self.find(self.count-1)] - 1

class Solution:
    def hitBricks(self, grid, hits):
        R = len(grid)
        C = len(grid[0])
        block = []
        
        def index(row, col):
            return row*C+col
        
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        A = [row[:] for row in grid]
        for i,j in hits:
            A[i][j] = 0

        wqu = WeightQU(R*C+1)
        for r,row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r,c)
                    if r == 0:
                        wqu.union(i,R*C)
                    if r and A[r-1][c]:
                        wqu.union(i,index(r-1,c))
                    if c and A[r][c-1]:
                        wqu.union(i,index(r,c-1))
        
        ans = []
        for r,c in reversed(hits):
            pre_roof = wqu.number()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r,c)
                for nr,nc in neighbors(r,c):
                    if A[nr][nc]:
                        wqu.union(i,index(nr,nc))
                if r == 0:
                    wqu.union(i,R*C)
                A[r][c] = 1
                ans.append(max(0,wqu.number()-pre_roof-1))
        ans.reverse()
        return ans
# @lc code=end
sol = Solution()

grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,1],[1,0]]

res = sol.hitBricks(grid,hits)

print(res)
