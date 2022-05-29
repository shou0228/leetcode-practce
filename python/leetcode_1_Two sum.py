#此為暴力解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # 因為要返回的是索引，所以應該使用陣列的索引進行迴圈 
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j] #此印出結果為0,1為位元位置 符合2+7=9

                  
                  
                  
                 
