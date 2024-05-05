class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm={}
        highest=0
        sum = 0
        for i in nums:
            hm[i]=hm.get(i,0)+1
            if hm[i]>highest:
                highest = hm[i]
                sum=0
            
            if hm[i]==highest:
                sum+=hm[i]
                
        return sum
                
                
            