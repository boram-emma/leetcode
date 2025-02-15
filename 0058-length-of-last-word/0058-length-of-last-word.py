class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nws = s.split(' ')
        for i in range(-1,-len(nws)-1,-1):
            if nws[i] == ' ':
                pass
            else:
                return len(nws[i])