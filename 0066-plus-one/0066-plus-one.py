class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        if digits[i] != 9:
            digits[i] += 1
            return digits
        while (digits[i] == 9):
                
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
                return digits
            i=i-1
        digits[i] +=1
        return digits
        
            
