def hpapply(data, m, sort = True):

    # verify data is integer, string or list
    data_is_int = isinstance(data, int)
    data_is_str = isinstance(data, str)
    data_is_list = isinstance(data, list)
    if data_is_int:
        n = data
        data = list(range(data))
    elif data_is_str:
        n = len(data)
    elif data_is_list:
        n = len(data)
        if sort:
            data.sort()
    else:
        raise Exception("Unsupported data type {}".format(type(data)))

    # generate combination

    l = [0] * m
    
    while True:

        yield [data[i] for i in l]

        l[m - 1] += 1

        for i in reversed(range(m)):
            if l[i] == n:
                l[i] = 0
                if i != 0:
                    l[i - 1] += 1
                else:
                    return

# hpapply(7, 4, print)
# hpapply([7,6,5], 4, print)
# hpapply([7,6,5], 4, print, sort = False)
# hpapply("meow", 4, print)
# hpapply(2, 4, print)