class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        postfix = []
        running_prod=1
        for num in nums:
            running_prod *= num
            prefix.append(running_prod)
        
        running_prod=1
        for num in reversed(nums):
            running_prod *= num
            postfix.append(running_prod)
        postfix = list(reversed(postfix))
        res =[]
        print postfix
        print prefix
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[1])
            elif i == (len(nums))-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        
        return res