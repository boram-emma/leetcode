class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = cleaned_s.lower()

        left = 0
        right = len(s) -1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        if left >= right:
            return True


