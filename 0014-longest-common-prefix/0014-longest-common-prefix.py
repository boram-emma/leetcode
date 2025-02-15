class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        strs.sort()
        first = strs[0]
        last = strs[-1]
        leng = min(len(first), len(last))

        common_prefix = []

        for i in range(0,leng):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break
        
        return "".join(common_prefix)