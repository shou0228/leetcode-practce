#此為暴力解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # 因為要返回的是索引，所以應該使用陣列的索引進行兩次for迴圈 跑兩次分別找出兩個相加為9的數字
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j] #此印出結果為0,1為位元位置 符合2+7=9

                  
#hash table 涉及是否存在的問題都可用雜湊表                  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #雜湊表
        dict = {}
        for i,j in enumerate(nums):
            if target-j in dict:
                return [dict[target-j],i]
            dict[j] = i                        
                 
