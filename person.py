class student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def show_me(self):
        print(f'我的名字叫{self.name},我今年{self.age}岁了')


if __name__ == '__main__':
    student1 = student("李华",18)
    student1.show_me()