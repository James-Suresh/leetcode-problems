class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls=0
        cows=0
        hm={}
        
        ignore=[]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                ignore.append(i)
            elif secret[i] in hm:
                hm[secret[i]]+=1
            else:
                hm[secret[i]]=1
                    

        for i in range(len(guess)):
            if i in ignore:
                continue
            if guess[i] in hm:
                if hm[guess[i]]>0:
                    hm[guess[i]]-=1
                    cows+=1
        
        return str(bulls)+"A"+str(cows)+"B"