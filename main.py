from stack import Stack


def test_integers():
    s = Stack(1)
    s.push(5)
    t = s.pop()
    print(t)


def test_floats():
    x = Stack(1.1)
    x.push(1.20)
    t = x.pop()
    print(t)
    pass


def test_strings():
    y = Stack('asd')
    y.push("word")
    t = y.pop()
    print(t)


def test_all():
    b = Stack()
    b.push(9)
    b.push("This is a string")
    b.push(99.99)
    t = b.pop()
    y = b.pop()
    u = b.pop()
    print(t)
    print(y)
    print(u)


if __name__ == '__main__':
    test_integers()
    test_floats()
    #test_strings()
    #test_all()
