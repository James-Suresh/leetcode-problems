class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, br = a[::-1], b[::-1]
        res=""
        carry=0
        for i in range(max(len(a), len(b))):
            if i<len(br) and i<len(ar):
                if ar[i] == br[i]:
                    if ar[i]=='1':
                        if carry == 0:
                            res+="0"
                        else:
                            res+="1"
                        carry=1
                    else:
                        if carry == 0:
                            res+="0"
                        else:
                            res+="1"
                        carry=0
                else:
                    if carry==0:
                        res+="1"
                    else:
                        res+="0"
                        carry=1
            elif len(ar)>len(br):
                if carry==0:
                    res+=ar[i:]
                    break
                else:
                    if ar[i]=="1":
                        res+="0"
                    else:
                        res+="1"
                        carry=0
                    
            else:
                if carry==0:
                    res+=br[i:]
                    break
                else:
                    if br[i]=="1":
                        res+="0"
                    else:
                        res+="1"
                        carry=0
        if carry==1:
            res+="1"

        return res[::-1]
        
            

                        
                


