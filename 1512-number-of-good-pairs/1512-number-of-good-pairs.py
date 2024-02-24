class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            nums2=nums[i+1:]
            for j in range(len(nums2)):
                if nums[i]==nums2[j]:
                    res += 1
        
        return res
                    
            
            