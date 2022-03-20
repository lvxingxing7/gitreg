# class gcat():
#     def __init__(self,name,top,acc):
#         self.name = name
#         self.top = top
#         self.acc = acc
    
    # def __lt__(self,other):
    #     return self.acc < other.acc
        
#     def show(self):
#         return self.name,self.top,self.acc

# car1 = gcat('aaa',100,7)
# car2 = gcat('aaa',150,6)
# car3 = gcat('aaa',160,9)
# car_list = [car1.show(),car2.show(),car3.show()]
# car_list.sort()
# print(type(car_list.sort()))



class Preson:

    def __init__(self,name:str,age:int,sex:str) -> None:
        self.name = name
        self.age = age
        self.sex = sex


    def eat(self):
        print(f'{self.name}正在吃')

    def watch_av(self):
        print(f'{self.name}正在收看av')

class Student(Preson):
    
    def __init__(self, name: str, age: int, sex: str,kecheng) -> None:
        super().__init__(name, age, sex)
        self.kecheng = kecheng

    def study(self):
        print(f'{self.name}正在学习{self.kecheng}')


stu = Student('a',18,'n','yuwen')

stu.study()