"""
v = s/t
1 - t = s/v -> t = target/v = (50-10)/2 = 20 h
2 - t = 9 h -> 9 <= 20 -> THE SAME FLEET!
position = [3,5,2,10] -> [10,5]
speed = [10,5,8,2]
target = 50
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted([(pos,speed) for pos,speed in zip(position,speed)], reverse = True)
        stack = []
        num_fleet = 0

        for car in sorted_cars:
            hours_to_target = (target-car[0]) / car[1]
            if not stack or hours_to_target > stack[-1]:
                stack.append(hours_to_target)
        return len(stack)
            
            


