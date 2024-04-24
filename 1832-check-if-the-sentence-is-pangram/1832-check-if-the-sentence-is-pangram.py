class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = set(list("thequickbrownfoxjumpsoverthelazydog"))
 
        counter=0
        for l in sentence:
            if l in letters:
                letters.remove(l)
                counter+=1
        if counter == 26:
            return True
        return False