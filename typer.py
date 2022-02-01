import random


def sizeof(max_num, ctype='tuple'):
    items_size = 0
    if ctype == 'tuple':
        c = ()
        for i in range(1, max_num + 1):
            c = c + (i, )
            items_size += i.__sizeof__()
    elif ctype == 'list':
        c = []
        for i in range(1, max_num + 1):
            c.append(i)
            items_size += i.__sizeof__()
    elif ctype == 'set':
        c = set()
        for i in range(1, max_num + 1):
            c.add(i)
            items_size += i.__sizeof__()
    else:
        raise ValueError("unknown type")

    cont_size = c.__sizeof__()
    max_size = items_size + cont_size
    return (items_size, cont_size, max_size)


def sizeofrand(max_num, ctype='tuple'):
    items_size = 0
    rand = lambda: random.randint(0, 10)
    if ctype == 'tuple':
        c = ()
        while max_num > 0:
            i = rand()
            c = c + (i, )
            items_size += i.__sizeof__()
            max_num -= 1
    elif ctype == 'list':
        c = []
        while max_num > 0:
            i = rand()
            c.append(i)
            items_size += i.__sizeof__()
            max_num -= 1
    elif ctype == 'set':
        c = set()
        while max_num > 0:
            i = rand()
            c.add(i)
            items_size += i.__sizeof__()
            max_num -= 1
    else:
        raise ValueError("unknown type")

    cont_size = c.__sizeof__()
    max_size = items_size + cont_size
    return (items_size, cont_size, max_size)


def print_sizes(ctype='tuple', rand=True, scale="lin"):
    step = 0
    size_steps = 20
    current_cont_size = 0
    print("   Len      Items       Cont        Max")
    while size_steps:
        if scale == "lin":
            n = step
        elif scale == "log":
            n = 2**step - 1
        else:
            raise ValueError("unknown scale")

        if rand:
            s = sizeofrand(n, ctype)
        else:
            s = sizeof(n, ctype)

        if s[1] > current_cont_size:
            print('{0:6d} {1:10d} {2:10d} {3:10d}'.format(n, s[0], s[1], s[2]))
            current_cont_size = s[1]
            size_steps -= 1

        step += 1


def print_compared(number):
    t = sizeof(number, ctype='tuple')
    l = sizeof(number, ctype='list')
    s = sizeof(number, ctype='set')
    print(number, t[0], t[1], l[1], s[1])


print_compared(10**4)
print_sizes(scale='log')
print_sizes('list', scale='log')
