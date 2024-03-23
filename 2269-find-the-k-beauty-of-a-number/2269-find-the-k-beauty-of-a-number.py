class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        res=0
        snum = str(num)
        for i in range(0, len(snum)-k+1, 1):
            nsubstr=int(snum[i:k+i])
            if nsubstr>0 and num%nsubstr==0:
                res+=1
            
        return res
                
            