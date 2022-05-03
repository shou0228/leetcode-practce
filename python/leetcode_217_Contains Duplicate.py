#暴力解#sort
class Solution(object):
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in xrange(0, len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
            
        return False
        
#map#字典解法
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in nums:
            if i in map:
                return True
            map[i] = True
            
        return False
              
#最佳解 #set
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        
        
        
