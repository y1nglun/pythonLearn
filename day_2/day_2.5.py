def abc(a, *args):
    print(a)
    print(args)


abc(100, 200, 300, 400, 500, 200)


def bcd(a, **kwargs):
    print(a)
    print(kwargs)


bcd(100, x=200, y=300, z=400)
