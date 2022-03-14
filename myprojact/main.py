import math
import os
import random

# class Student:

#     def __init__(self,name:str,age:int,sex:str) -> None:
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def study(self,kecheng):
#         print(f'{self.name}正在学习{kecheng}')

#     def eat(self):
#         print(f'{self.name}正在吃')

#     def watch_av(self):
#         print(f'{self.name}正在收看av')


class Circle:

    def __init__(self,redius:float) -> None:
        self.redius = redius

    def perimeter(self):
        return 2 * self.redius * math.pi

    def area(self):
        return math.pi * self.redius ** 2


# if __name__ == '__main__':
#     r = float(input('请输入你的半径:'))
#     small , big = circle(r) ,circle(r+3)
#     perimeter_cost = big.perimeter() * 38.5
#     area_cost = small.area() * 18.5
#     print(f'围墙成本为{perimeter_cost:.2f}')
#     print(f'泳池成本为{area_cost:.2f}')


class Clock:

    def __init__(self,hours=0,minutes=0,seconds=0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def run(self):
        self.seconds += 1
        if self.seconds == 60 :
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60 :
                self.minutes = 0
                self.hours += 1

    def show(self):
        return (f'{self.hours:0>2d}:{self.minutes:0>2d}:{self.seconds:0>2d}')

# if __name__ == '__main__':
#     clock = Clock()
#     while True:
#         os.system('cls')
#         print(clock.show())
#         sleep(1)
#         clock.run()

class Card:
    def __init__(self,clor,num) -> None:
        self.clor = clor
        self.num = num

    def __repr__(self) -> str:
        return self.show()

    def show(self):
        suites =  {'s': '♠','h':'♥','c':'♣','d':'♦'}
        faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return f'{suites[self.clor]}{faces[self.num]}'


def exit():
    a = Card('s',2)
    print(a)

# if __name__ == '__main__':
#     exit()

class Poke:

    def __init__(self):
        self.poke_list = []
        for su in 'shcd':
            for fa in range(1,14):
                car = Card(su,fa)
                self.poke_list.append(car)
        self.count = 0
    
    def shuffle(self) -> list: 
        self.count = 0
        random.shuffle(self.poke_list)

    def give_cars(self):
        cars = self.poke_list[self.count]
        self.count += 1
        return cars

    def has_more(self) -> bool: 
        return self.count < len(self.poke_list)

lst = Poke()
lst.shuffle()
print(lst.poke_list)
while lst.has_more():
    print (lst.give_cars())
