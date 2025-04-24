class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, path, 1, n, k)
        return result
    
    def traversal(self, result, path, startIndex, n, k):
        if sum(path)==n and len(path)==k:
            result.append(path[:])
            return 
        if sum(path)>n or len(path)>k:
            return

        for i in range(startIndex, 10):
            path.append(i)
            self.traversal(result, path, i+1, n, k)
            path.pop()
        