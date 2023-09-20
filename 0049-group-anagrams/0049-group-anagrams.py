class Solution(object):
    def groupAnagrams(self, strs):
        output = collections.defaultdict(list)
        for s in strs :
            #creating empty key list for each alphabet
            key = [0] * 26
            for char in s : 
                #key list gets populated based on the word
                key[ord(char) - ord('a')] +=1
            #anagrams will be appended to outputdictionary, all anagrams will have same key
            output[tuple(key)].append(s)

            #returning outputs
        return output.values()