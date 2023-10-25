class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        phone={}
        res=[]
        c=0
        
        if digits == "":
            return res
        for i in range(8):
            if(i+2==7 or i+2==9):
               phone[i+2]=[]
               while len(phone[i+2])<4:
                     phone[i+2].append(chr(c+97))
                     c+=1
            else:
                phone[i+2]=[]
                while len(phone[i+2])<3:
                     phone[i+2].append(chr(c+97))
                     c+=1

        def comb(num, word,idx):
            if len(num)==1:
             
                word+=phone[int(num)][idx]
                res.append(word)
               
                
                    


            else:
                print len(num)
 
                word+=phone[int(num[0])][idx]
                if num[1]=='7' or num[1]== '9':
                    r=4
                else:
                    r=3
                for k in range(r):
                    comb(num[1:], word, k)
        
        comb(digits,"",0)
        comb(digits,"",1)
        comb(digits,"",2)

        if digits[0]== '7' or digits[0]=='9':
            comb(digits,"",3)

        return res

        