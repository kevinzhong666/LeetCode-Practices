class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {"}": "{", ")": "(", "]": "["}

        for char in s:
            # Check if char is an opening bracket
            if char in bracket_map.values():
                stack.append(char)
            # Check if char is a closing bracket
            elif char in bracket_map:
                # If the stack is empty or the top element of the stack does not match the corresponding opening bracket
                if not stack or bracket_map[char] != stack.pop():
                    return False
            # If char is not a bracket, you may choose to ignore it or handle differently
        # After processing all characters, return True if the stack is empty, indicating a valid string
        return not stack
