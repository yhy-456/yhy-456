import pytest

z={'a': 1, 'b':2}
x={'a': 3, 'b':4}

data=[{'a': 1, 'b':2},{'a': 3, 'b':4}]

@pytest.fixture(params=data)
def test_z(request):
    #print("111111",request.param)
    return request.param


class Test_A:
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup__method")

    def teardown(self):
        print("teardown__method")
    def test_a(self,test_z):
        print(test_z)
        #print(test_z['a'],test_z['b'])
        print("--------test_a")

    # def test_a1(self):
    #     #print(loginn)
    #     print('111111111111111111111111122222222222')
        #print(test_z['a'],test_z['b'])
        #print("--------test_a")
    #
    # #@pytest.mark.skipif(condition=2 > 1, reason="跳过该函数")
    # @pytest.mark.parametrize("abc",[1,2,3])
    # def test_b(self,abc):
    #     print("--------test_b")
    #     print(abc)
    #
    # @pytest.mark.parametrize("a,b", [(1, 2), (3,4)])
    # def test_c(self, a,b):
    #     print("--------test_b")
    #     print(a)




if __name__=='__main__':
    pass
    #print('222')
    #print(pytest.__version__)
    #pytest.main("-s test_a.py")
    #print(pytest.fixture())