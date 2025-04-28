# 1. dp数组以及下标的含义：从左上角到右下角到达grid[i][j]时的最小路径和
# 2. 递推公式：
# dp[i][j]=min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
# 3. 初始化：dp[0][0]=0 dp[0][j]=dp[0][j-1]+grid[0][j] dp[i][0]=dp[i-1][0]+grid[i][0]
# 4. 遍历顺序：从左到右，从上到下

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0]*len(grid[0]) for _ in range(len(grid))] # 列为grid[0]，行为grid
        dp[0][0]=grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j]=min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[-1][-1]