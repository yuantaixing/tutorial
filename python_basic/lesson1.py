def hello():
    print("hello world!")
    pass


def genre_test():
    """基本数据类型"""
    a = 1
    b = "hello"
    c = True
    d = [1, 2, 3, 4]
    e = (1, 2, 3, 4)
    f = {"name": "jack", "age": 10}
    print("type of a is:", type(a))
    print("type of b is:", type(b))
    print("type of c is:", type(c))
    print("type of d is:", type(d))
    print("type of e is:", type(e))
    print("type of f is:", type(f))
    pass


def int_float_str_test():
    a = 1
    print("a:", a)
    print("a+1:", a + 1)
    b = a + 1
    print("b:", b)
    b = b + 1
    print("b:", b)
    b += 1
    print("b:", b)
    c = a + 1.0
    print("c:", c)
    # d = a+"hello"
    d = str(a) + "hello"
    e = str(a) + "2"
    print("d:", d)
    print("e:", e)

    pass


def str_test():
    b = "hello"
    print(b)
    print(b[0])
    print(b[-1])
    pass


def list_test():
    d = [1, 2, 3, 4]
    print(d)
    print(d[0])
    print(d[-1])
    print(d[0:2])
    print(d[:2])
    print(d[:-1])
    print(d[0])
    d[0] = "hello"
    print(d[0])
    print(d)


def tuple_test():
    e = (1, 2, 3, 4)
    print(e)
    print(e[0])
    pass


def dict_test():
    f = {"name": "jack", "age": 10}
    print(f)
    print(f.keys())
    print(f.values())
    print(f.items())

    pass


def set_test():
    pass


if __name__ == '__main__':
    """"""
    # genre_test()
    # int_float_str_test()
    # str_test()
    # dict_test()
