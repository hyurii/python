def suma(a, b):
    print locals().values()
    z = a+1
    y = b+1
    print locals().values()
    print locals()
    return z, y

print suma(2, 1)
