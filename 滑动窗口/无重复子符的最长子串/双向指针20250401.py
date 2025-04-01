# 时间复杂度：O(n)
# 和前面的题目类似，也是看left+=1的最多次数
# 空间复杂度：O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0 # 无重复字符的最长子串的长度
        cnt=Counter() # hashmap 最多有128个字符，因此空间复杂度是O(1)
        left=0 # 标记当前无重复字符子串的起始位置
        for right in range(len(s)): # right表示当前正在考虑的字符的位置
            cnt[s[right]]+=1 # 在计数器中加1，表示该字符在当前子串中又出现了一次
            # 处理重复字符：该字符在当前子串中出现了重复，此时移动左指针，直到该子串中没有重复的子串
            while cnt[s[right]]>1: 
                cnt[s[left]]-=1
                left+=1
            ans=max(ans, right-left+1) # 字符个数（一定是right-left+1，因为当right和left指向同一个字符的时候子串长度为1）
        return ans
        