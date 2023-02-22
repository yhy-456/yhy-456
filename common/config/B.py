from common.config.A import A

class B(A):
    def __init__(self,a,c,b):
        super().__init__(a,c)
        self.b = b

    def func_b(self):
        #print("1")
        self.func_a()
        print(self.b)
        print(self.c)


if __name__=='__main__':
    b = B(2,1,3)
    b.func_b()
    #print(b.func_b())