class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        hm  = {}
        res=0
        
        for i in nums:
            hm[i] = hm.get(i, 0) + 1
            
        for i in hm.keys():
            print hm[i]
            if hm[i] == 1:
                res+=i
        return res
                
                