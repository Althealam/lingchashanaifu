# 增加左括号和右括号的数量来进行剪枝
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        path=[]
        left=0 # 左括号的数量
        right=0 # 右括号的数量
        self.traversal(result, path, n, left, right)
        return result
    
    def traversal(self, result, path, n, left, right):
        # 字符串长度已经达到了收割条件
        if len(path)==2*n:
            result.append(''.join(path))
            return 
        if left<n:
            path.append('(')
            self.traversal(result, path, n, left+1, right)
            path.pop()
        if right<left: # 注意：本题需要生成的是有效的括号组合，因此right一定要小于left才可以
            path.append(')')
            self.traversal(result, path, n, left, right+1)
            path.pop()

        