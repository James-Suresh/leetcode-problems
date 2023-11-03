class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        while(l<len(nums)):  
            if nums[l]==0:
                nums.pop(l)
                nums.insert(0,0)
           
            l+=1        
            
        while r>=0: 
            if nums[r]==2:
                nums.pop(r)
                nums.append(2)      
            r-=1
            
       
