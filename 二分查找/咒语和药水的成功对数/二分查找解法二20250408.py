# 对potions进行排序，可以利用有序性进行二分查找
# 对于每个咒语spells[i](0<=i<n)，计算出目标值target=success/spells[i]（目前是spell*potion>=success，那么potion的目标值就是success/spell)
# 利用二分查找来在数组potions中找到第一个大于等于target的元素的索引idx，进一步可以得到表示成功组合的药水数量len(potions)-idx

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions)-bisect.bisect_right(potions, (success-1)//i) for i in spells]
    
    # def search(self, potions, success):
    #     """
    #     找到第一个大于等于success的元素下标，并且potions是有序的
    #     """
    #     left=0
    #     right=len(potions)-1
    #     if potions[right]<success:
    #         return -1
    #     while left<=right:
    #         mid=(left+right)//2
    #         if potions[mid]<success: # [mid+1, len(potions)-1]
    #             left=mid+1
    #         elif potions[mid]>success: # [0, mid-1]
    #             right=mid-1
    #         else:
    #             return mid
    #     return left 

        