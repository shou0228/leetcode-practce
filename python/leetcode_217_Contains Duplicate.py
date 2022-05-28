#暴力解#sort＃在Python3中，range()與xrange()統一合並為range()
class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for i in range(0, len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
            

#最佳解 #set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
        
        
        
