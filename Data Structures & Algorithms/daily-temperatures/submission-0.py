class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        indexes_stack = []

        for idx,elem in enumerate(temperatures):
            while (stack and elem > stack[-1]):
                output[indexes_stack[-1]] = idx - indexes_stack[-1]
                stack.pop()
                indexes_stack.pop()
            stack.append(elem)
            indexes_stack.append(idx)
        
        return output

#stack = [30], indexes_stack[0]
#output = [1,], stack = [38], indexes_stack = [1]
#output = [1,0,0...], stack = [38,30], indexes_stack = [1,2]
#output = [1,0,1], stack = [38,36], indexes_stack = [1,3]
#output = [1,0,1,0], stack = [38,36,35], indexes_stack = [1,3,4]
#output = [1,0,1,1], stack = [38,36], indexes_stack = [1,3]
#output = [1,0,2,1]