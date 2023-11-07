class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        i=0
        while i < len(nums):
            if nums[i] in hm:
                if hm[nums[i]]<2:
                    hm[nums[i]] +=1
                else:   
                    nums.pop(i)
                    i-=1
            else: 
                hm[nums[i]]=1
            i+=1
      
        return len(nums)