class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res=[]
        hm={}
        carry=0
        nums_sort = nums[:]
        nums_sort.sort()
        for i,n in enumerate(nums_sort):
            if (i == 0):
                hm[n]=0
            else:
                carry+=1
                if nums_sort[i-1]!=n:
                    hm[n] = hm.get(n,0) + carry
                   
                    
        for i in nums:
            res.append(hm[i])
            
        return(res)
                    
        
            