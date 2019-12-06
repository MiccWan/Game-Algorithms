def happly(data, m, callback, sort = True):

    # verify data is integer, string or list
    data_is_int = isinstance(data, int)
    data_is_str = isinstance(data, str)
    data_is_list = isinstance(data, list)
    if data_is_int:
        n = data
    elif data_is_str:
        n = len(data)
    elif data_is_list:
        n = len(data)
        if sort:
            data.sort()

    def applyRepSelections():

        l = [0] * m
        
        while True:

            # apply the given callback
            if data_is_int:
                callback(l.copy())
            elif data_is_str:
                callback("".join([data[i] for i in l]))
            else:
                callback([data[i] for i in l])

            f_found = False
            
            for i in reversed(range(m)):
                if l[i] < n - 1:
                    f_found = True
                    break

            if not f_found:
                return

            l[i] = l[i] + 1
            for j in range(i+1, m):
                l[j] = l[i]

    applyRepSelections()

# happly(7, 4, print)
# happly([0,1,2,3], 4, print)
# happly([4,3,0], 4, print)
# happly([4,3,0], 4, print, sort = False)
# happly("7654321", 4, print)