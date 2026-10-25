class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda x: x[0])
        cars_t = [(target - car[0]) / car[1] for car in cars]
        n = len(cars_t)
        stack = []
        for i in range(n - 1, -1, -1):
            if stack and cars_t[stack[-1]] >= cars_t[i]:
                continue
            stack.append(i) 

        return len(stack)