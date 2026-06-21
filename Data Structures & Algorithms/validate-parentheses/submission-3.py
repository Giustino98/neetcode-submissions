

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_closed_open = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char not in map_closed_open: stack.append(char)
            else:
                if not stack or stack.pop() != map_closed_open[char]: return False
        return not stack
        