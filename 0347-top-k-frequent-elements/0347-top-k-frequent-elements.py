class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        mostfreq = [0]*k
        numdict = collections.defaultdict(lambda: 0)
        for i in range(len(nums)):
            numdict[nums[i]] += 1
          
        numdict = sorted(numdict.items(), key=lambda x: x[1],reverse = True)
        
        for i in range(len(mostfreq)):
            mostfreq[i]=numdict[i][0]
        return mostfreq
        
        
            
        #for i in range (len(numlist)):
            
            
            
        
         