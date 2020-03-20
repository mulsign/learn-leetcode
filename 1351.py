class Solution:
    def countNegatives(self, grid) -> int:
        ans = 0
        i,j = 0,0
        M = len(grid)
        N = len(grid[0])
        while(i<M):
            j = 0
            while(j<N):
                if(grid[i][j]<0):
                    ans += (M-i)*(N-j)
                    N = j
                    break
                j += 1
            i += 1

        return ans
                
sol = Solution()

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(sol.countNegatives(grid))

