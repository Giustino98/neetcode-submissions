class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos,sp) for pos,sp in zip(position,speed)]
        cars.sort(reverse=True)
        res = []

        for car in cars:
            time_to_target = (target-car[0])/car[1]
            if not res: res.append(time_to_target)
            if time_to_target > res[-1]: res.append(time_to_target)
        
        return len(res)
