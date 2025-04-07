# 思路：本题和“长度最小的子数组”类似，都是最短型的滑动窗口（本题t是需要寻找的子串，s是被寻找的字符串）
# 1. 初始化ansleft=-1，ansright=len(s)，用来记录最短子串的左右端点
# 2. 用一个哈希表cntT来存储t中每个字母的出现次数
# 3. 初始化left=0和一个空哈希表cntS用来统计s子串中每个字母的出现次数
# 4. 遍历s，当前枚举的子串右端点为right，将s[right]+=1
# 5. 遍历cntS中的每个字母以及出现次数，如果出现次数都大于等于cntT中的字母出现次数
# （1）right-left<ansRight-ansLeft：找到了更短的子串，ansLeft=left, ansRight=right
# （2）s[left]的出现次数-1
# （3）left+=1
# （4）重复上述的步骤，直到cntS有字母的出现次数小于cntT中该字母的出现次数为止

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right=-1, len(s)
        cnt_s=Counter() # s子串字母的出现次数
        cnt_t=Counter(t) # t中字母的出现次数
        left=0
        for right in range(len(s)):
            cnt_s[s[right]]+=1 # 右端点字母在考虑的子串范围内
            while cnt_s>=cnt_t: # 目前考虑的子串涵盖了目标子串t
                if right-left<ans_right-ans_left:
                    ans_left, ans_right=left, right # 更新子串
                cnt_s[s[left]]-=1 # 左端点字母移出子串，继续寻找更短的子串
                left+=1
        return '' if ans_left<0 else s[ans_left:ans_right+1]
        