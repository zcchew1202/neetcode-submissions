from operator import itemgetter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for car in zip(position,speed):
            cars.append(car)
        if len(cars) == 1:
            return 1
        cars.sort(key=itemgetter(0), reverse=True)
        stack = []
        res = []
        for car in cars:
            pos, speed = car
            time = (target - pos)/speed
            if stack:
                stack_t = (target - stack[-1][0])/stack[-1][1]
                if time > stack_t:
                    stack.append(car)
            else:
                stack.append(car) 


        return len(stack)