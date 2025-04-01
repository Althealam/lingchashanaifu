class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans=0 # 统计最长的半重复子字符串的长度
        left=0
        count=0 # 统计该滑动窗口内的相邻相等字符对个数
        for right in range(len(s)):
            if right>0 and s[right]==s[right-1]:
                count+=1
            while count>1:
                count-=1
                left+=1
            ans=max(count, right-left+1)
        return ans
        
sol=Solution()
s="524446"
result=sol.longestSemiRepetitiveSubstring(s)
print(result)