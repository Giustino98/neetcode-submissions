class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = sorted([(pos,speed) for pos,speed in zip(position,speed)],reverse=True)
        stack = []

        for pos,speed in array:
            time_to_arrive = (target - pos)/speed
            if not stack or time_to_arrive > stack[-1]: stack.append(time_to_arrive)

        return len(stack)