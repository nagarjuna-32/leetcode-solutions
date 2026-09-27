class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = []
        
        for char in s:
            if char == '(':
                stack.append(current)
                current = []
            elif char == ')':
                current.reverse()
                prev = stack.pop()
                prev.extend(current)
                current = prev
            else:
                current.append(char)
                
        return "".join(current)