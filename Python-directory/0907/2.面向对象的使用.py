# 当前时间： 2021-09-06 11:37

class Person:
    def __init__(self,name:str,sex:str='男',hobby:str='游戏') -> None:
        self.name=name
        self.sex=sex
        self.hobby=hobby
    def eat(self)-> None:
        print('吃饭')
    def study(self,info)-> None:
        print(f'{info}')
    def show_me(self)-> str:
        return f'{self.name,self.hobby}'

p1=Person('张三','女','喝酒')
print(p1.show_me())