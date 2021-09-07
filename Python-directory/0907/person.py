# 当前时间： 2021-09-06 13:04
class student:
    def __init__(self,name:str,age:int)->None:
        self.name=name
        self.age=age
    def show_me(self):
        return f'我是{self.name},{self.age}岁'

