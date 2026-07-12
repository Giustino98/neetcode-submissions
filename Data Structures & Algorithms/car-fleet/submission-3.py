class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_sorted = sorted([(pos,sp) for pos,sp in zip(position,speed)], reverse=True)
        stack = []

        for pos,sp in cars_sorted:
            time_to_arrival = (target-pos) / sp
            if not stack: stack.append(time_to_arrival)
            elif time_to_arrival > stack[-1]: stack.append(time_to_arrival)

        return len(stack) 
