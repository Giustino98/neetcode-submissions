class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for idx,temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                pop_idx = stack.pop()
                output[pop_idx] = idx - pop_idx
            stack.append(idx)
        return output
            