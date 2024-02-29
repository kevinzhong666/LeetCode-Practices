class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')':
                if not stack or stack.pop() != '(':
                    return False
            if char == ']':
                if not stack or stack.pop() != '[':
                    return False
            if char == '}':
                if not stack or stack.pop() != '{':
                    return False
        # Edge for
        # "[" or "{" or "("
        if stack:
            return False
        return True