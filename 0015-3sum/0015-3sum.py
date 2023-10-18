class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i,n in enumerate (nums):
            if n > 0:
                break
            p1=i+1
            p2 = len(nums)-1
            if i > 0 and n == nums[i - 1]:
                continue
            while(p1<p2):
                if(nums[p1]+nums[p2]+n==0):
                    a=[nums[p1],nums[p2],n]
                    res.append(a)
                    p1+=1
                    p2-=1
                    while nums[p1] == nums[p1-1] and p1 < p2:
                        p1+= 1
                elif(nums[p1]+nums[p2]+n>0):
                    p2-=1
                elif(nums[p1]+nums[p2]+n<0):
                    p1+=1

        return res
        
                


        