class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        path=[]
        result=[]
        max_len=0
        self.traversal(result, path, nums, target, 0)
        if len(result)==0:
            return -1
        for path in result:
            max_len=max(max_len, len(path))
        return max_len
    
    def traversal(self, result, path, nums, target, startIndex):
        if sum(path)==target:
            result.append(path[:])
            return 
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.traversal(result, path, nums, target, i+1)
            path.pop()
        