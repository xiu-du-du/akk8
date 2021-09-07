# 当前时间： 2021-09-06 12:05
class Student:
    def __init__(self,id:int,name:str,score:float,age:int)->None:
        self.id=id
        self.name=name
        self.score=score
        self.age=age
    def study(self,info)->None:
        print(f'正在学习{info}')
    def show_me(self)->str:
        return f'我是{self.name}，我的id是{self.id}，我的成绩是{self.score}，我的年龄是{self.age}'

allen=Student(1001,'Allen',90,18)
print(allen.show_me())
baby=Student(1002,'宝儿姐',100,20)
baby.study('挖坑')
print(baby.show_me())





