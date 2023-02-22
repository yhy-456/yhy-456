class A(object):
    def __init__(self, name):
        self.name = name  # 改成正常形式

    def fuMethod(self):
        print("fu method")


class B(A):
    def __init__(self, name, age):
        self.name = "zi name"  # 这里还是写成赋值形式，便于查看参数传递
        #print(self.name)
        self.age = age
        super().__init__(name)
        #print(self.name)

    def fuMethod(self, name, age):
        #self.__init__(name, age)
        self.name = "zzi name"  # 这里还是写成赋值形式，便于查看参数传递
        print(self.name)


b = B("immuable", 18)
print(b.name, b.age)

b.fuMethod("--", 18)
