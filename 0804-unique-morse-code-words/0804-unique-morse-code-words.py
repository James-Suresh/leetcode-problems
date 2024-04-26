class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse={}
        morsearr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lnum=ord('a')
        for c in morsearr:
            morse[chr(lnum)]=c
            lnum+=1
        
        hm={}
        out=set()
        for w in words:
            s=""
            for c in w:
                s+=morse[c]
            out.add(s)
        return len(out)
                
            
            

            
            