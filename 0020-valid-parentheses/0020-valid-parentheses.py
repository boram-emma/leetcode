class Solution:
    def isValid(self, s: str) -> bool:
        character = {')':'(', '}':'{', ']':'['}
        
        stack = []
        for char in s:
            if char in character:
                top = stack.pop() if stack else '#'
                if character[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack
            

