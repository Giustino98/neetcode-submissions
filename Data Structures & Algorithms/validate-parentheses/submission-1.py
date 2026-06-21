

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {"(", "{", "["}
        map_closed_open = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char in opening_brackets: stack.append(char)
            else:
                if stack:
                    if stack.pop() == map_closed_open[char]: continue
                return False
        return len(stack) == 0
        