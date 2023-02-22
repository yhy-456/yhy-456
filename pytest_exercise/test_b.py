import pytest

@pytest.fixture()
def login():
    print('----进入--')
    a= 1
    yield a
    print('---返回---')



def test_b(login):
    #print(login)
    print('222')




