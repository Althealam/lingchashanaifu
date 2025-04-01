class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans=0 # 统计最长的半重复子字符串的长度
        left=0
        count=0 # 统计该滑动窗口内的相邻相等字符对个数
        for right in range(len(s)):
            # 检查是否有重复的字符，有的话则加1
            if right>0 and s[right]==s[right-1]:
                count+=1
            # 当重复次数超过1，收缩窗口
            while count>1:
                # 当left和left-1的元素值相同的时候，则将count减去1
                if s[left]==s[left+1]:
                    count-=1
                left+=1
            # 更新最大长度
            ans=max(ans, right-left+1)
        return ans
        