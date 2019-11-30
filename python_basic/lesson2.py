def if_test_1():
    a = 3
    if a > 3:
        print("a 大于3")

    pass


def if_test_2():
    a = 3
    if a > 3:
        print("a 大于3")
    elif a == 3:
        print("a 等于3")
    # elif a < 3:
    else:
        print("a小于于3")

    pass


def for_test_1():
    d = [1, 2, 3, 4]
    for item in d:
        print(item)
    pass


def for_test_2():
    f = {"name": "jack", "age": 10}
    # for item in f.items():
    #     print(item)

    # for item in f.keys():
    #     print(item)
    # for item in f.values():
    #     print(item)
    for key, value in f.items():
        print(key, ":", value)


def for_test_3():
    d = [1, 2, 3, 4]
    for item in d:
        if item == 2:
            print("got it:", item)
        else:
            print(item)
    pass


def for_test_4():
    d = [1, 2, 3, 4]
    for item in d:
        if item == 2:
            print("got it:", item)
            return
        else:
            print(item)
    pass


def while_test1():
    i = 0
    while True:
        if i > 10:
            return
        print(i)
        i = i + 1

    pass


if __name__ == '__main__':
    """"""
    # if_test_1()
    # if_test_2()
    # for_test_1()
    # for_test_2()
    # for_test_3()
    # while_test1()
