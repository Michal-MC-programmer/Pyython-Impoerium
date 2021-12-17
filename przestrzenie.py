a = 1  # globalna


# print(globals())
# print(locals())

def foo():
    b = 2

    def bar():
        print(a)
        print(b)
        print(globals())
        print(locals())

    # print(globals())
    # print(locals())
    # print(a)

    bar()

foo()
# bar()

def zmodyfikuj_a():
    # global a

    a = 10
    print(a)

zmodyfikuj_a()
print(a)


def zmodyfikuj():
    # global a
    b = 20
    def zmodyfikuj_b():
        nonlocal b
        b = 15

        print(b)

    zmodyfikuj_b()
    print(b)

zmodyfikuj()

# domknięcie
def increment_factory(step):

    def wrapper(liczba):
        return liczba + step

    return wrapper

incr_by_3 = increment_factory(3)
incr_by_5 = increment_factory(5)
print(incr_by_3(5))
print(incr_by_5(5))