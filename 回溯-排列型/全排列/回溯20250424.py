class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, nums, path)
        return result
    
    def traversal(self, result, nums, path):
        if len(path)==len(nums):
            result.append(path[:])
            return 
        if len(path)>len(nums):
            return 
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.traversal(result, nums, path)
            path.pop() 