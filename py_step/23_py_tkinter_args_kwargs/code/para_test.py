def test_func (*args) :
    print(args)


# 튜플로 반환
test_func(1,2,3,4,5)


def test_func2 (**kwargs) :
    print(kwargs)

test_func2(a=1, b='22', c = [1])
