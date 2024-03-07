class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.r, self.c = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        return self.solve(0, 0, obstacleGrid, memo)
    
    def solve(self, m, n, grid, memo={}):
        if (m >= self.r or n >= self.c): return 0
        if (grid[m][n] == 1): return 0
        if (m,n) in memo.keys(): return memo[(m,n)]
        if (m == self.r-1 and n == self.c-1): return 1
        

        memo[(m, n)] = self.solve(m+1, n, grid, memo) + self.solve(m, n+1, grid, memo)
        return memo[(m,n)]

        