""" Explains about variable no of args """

def hello(a, b, *args):
    print(a)
    print(b)
    print(args)

hello(10, 20, 30, 40, 'fifty')

