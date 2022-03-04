from distutils.command.clean import clean
import os
import math
from time import sleep, time



def filedoc(filename:str,doc:bool = False) -> str:
    finddoc = filename.rfind('.')
    if not doc :
        finddoc += 1
    return filename[finddoc:] if finddoc > 0 else ''
# if __name__ == '__main__':
#      print(filedoc('asc.py'))

def calcu ( init_value:int , fn , *args:int , **kwargs:int ) -> int:
    total = init_value
    for arg in args:
        if type(arg) in (int,float):
            total = fn(total,arg)
    for varg in kwargs.values():
        if type(varg) in (int,float):
            total = fn(total,varg)
    return total
# if __name__ == '__main__':
#      print(calcu(100,lambda x , y : x + y ,111))

def sort(lst:list,fn=lambda x , y : x > y ,resver:bool=False) -> list:
    new_lst = lst[:]
    for i in range (1,len(new_lst)):
        swap = False
        for j in range (0,len(new_lst) - i ):
            if fn (new_lst[j],new_lst[j + 1]):
                new_lst[j],new_lst[j+1] = new_lst[j+1],new_lst[j]
                swap = True
        if not swap :
            break
    return new_lst
# if __name__ == '__main__':
#      print(sort([11,53,73,24,73,57,64,23,78]))

def midfind(lst:list,nmb:int) -> int:
    start ,end = 0 ,len(lst) -1
    while start <= end:
        mid = (start + end) // 2
        if nmb > lst[mid]:
            start = mid + 1
        elif nmb < lst[mid]:
            end = mid - 1
        else:
            return mid
    return -1
# if __name__ == '__main__':
    # print(midfind([11, 23, 24, 53, 57, 64, 73, 73, 78],78))
     
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

