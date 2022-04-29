#Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#暴力解法
public boolean containsDuplicate_bruteforce(int[] nums) {
   if (nums == null || nums.length == 0) return false;
   
   int l = nums.length;
   for (int i=0; i<l; i++) {
      for (int j=i+1; j<l; j++) {
         if (nums[i] == nums[j]) {
            return true;
         }
      }
   }
   return false;
}
#O(n^2)
------------------------------------------------------------------------------------------------------
#排序解法
public boolean containsDuplicate(int[] nums) {
   if (nums == null || nums.length == 0) return false;
   
   Arrays.sort(nums);
   int l = nums.length;
   for (int i=1; i<l; i++) {
      if (nums[i-1] == nums[i]) {
         return true;
      }
   }
   return false;
#O(nlogn)O(nlogn)
 ------------------------------------------------------------------------------------------------------
 #最速解
 #HashSet 是一種包含所有唯一元素的數據結構，
 public boolean containsDuplicate_extraMemory(int[] nums) {
   if (nums == null || nums.length == 0) return false;
   
   Set<Integer> set = new HashSet<>();
   int l = nums.length;
   for (int i=0; i<l; i++) {
      if (set.contains(nums[i])) {
         return true;
      }
      set.add(nums[i]);
   }
   return false;
}
#O(1)



 

   
