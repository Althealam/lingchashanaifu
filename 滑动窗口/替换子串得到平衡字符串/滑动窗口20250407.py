# 分析：如果在待替换子串之外的任意字符的出现次数超过m=n/4，那么无论怎么替换，都无法使得这个字符在整个字符串中的出现次数为m
# 也就是说：如果在待替换子串之外的任意字符的出现次数都不超过m，那么可以通过替换，使得s为平衡字符串，即每个字符的出现次数都为m
# 思考：假设子串的左端点是left，右端点是right，如果子串外的任意字符的出现次数都不超过m，那么说明从left到right的这段子串可以是待替换子串，用其长度right-left+1更新答案的最小值，并右移left，缩小子串长度

class Solution:
    def balancedString(self, s: str) -> int:
        m=len(s)//4
        cnt=Counter(s) # 用来计算子串外的字符的出现次数（也就是left到right以外的子串的情况）
        ans=float('inf') # 记录待替换子串的长度
        left=0
        if len(cnt)==4 and max(cnt.values())==m: # 已经符合要求了
            return 0
        for right in range(len(s)):
            cnt[s[right]]-=1 # 减去出现的次数
            while max(cnt.values())<=m:
                ans=min(ans, right-left+1) # right-left+1是待替换子串可能的值
                cnt[s[left]]+=1
                left+=1 # 缩小子串
        return ans

        