class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for idx,temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                output[stack[-1]] = idx - stack[-1]
                stack.pop()
            else: stack.append(idx)
        return output
            