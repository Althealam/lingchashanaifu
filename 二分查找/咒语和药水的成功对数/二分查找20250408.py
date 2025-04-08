# 注意：这段代码还有问题，超出了时间限制
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[0]*len(spells) # 记录能和第i个咒语成功组合的药水数目
        for index, spell in enumerate(spells):
            current_potion=[]
            for potion in potions:
                current_potion.append(potion*spell)
            current_potion.sort() # 排序
            ind=self.search(current_potion, success)
            ans[index]=len(potions)-ind if ind!=-1 else 0
        return ans
    
    def search(self, potions, success):
        """
        找到第一个大于等于success的元素下标，并且potions是有序的
        """
        left=0
        right=len(potions)-1
        if potions[right]<success:
            return -1
        while left<=right:
            mid=(left+right)//2
            if potions[mid]<success: # [mid+1, len(potions)-1]
                left=mid+1
            else: # [0, mid-1]
                right=mid-1
        return left

        