class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        smallWord = min(word1, word2, key = len)
        abw = abs(len(word1)-len(word2))
        revisedW = smallWord + ' '*abw
        total = ''
        if smallWord == word1:
            for i in range(0,len(revisedW)):
                total = total + revisedW[i] + word2[i]
        else:
            for i in range(0,len(revisedW)):
                total = total + word1[i] + revisedW[i]
            
        aws = total.replace(" ", "")
        return aws


        