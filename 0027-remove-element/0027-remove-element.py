class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 #count
        numscopy=nums
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'    
            else:
                k += 1        
        c=len(nums)-k
        while(c>0):
            nums.remove('_')
            c-=1
        print nums
        return k

        