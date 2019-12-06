def papply(data, m, callback, sort = True):

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

    # generate combination
    def applySelections():
        
        l = list(range(m))
        
        while True:

            decSwapAlg(l.copy())
            f_found = False
            
            for i in reversed(range(m)):
                if l[i] < n - m + i:
                    f_found = True
                    break

            if not f_found:
                return

            l[i] = l[i] + 1
            for j in range(i+1, m):
                l[j] = l[i] + j - i

    # rearrange combination from cnm
    def decSwapAlg(l):

        while True:

            # apply the given callback
            if data_is_int:
                callback(l.copy())
            elif data_is_str:
                callback("".join([data[i] for i in l]))
            else:
                callback([data[i] for i in l])

            # keep generate next combination
            for i in reversed(range(m)):
                if i == 0:
                    return
                if l[i-1] < l[i]:
                    i = i - 1
                    break

            for j in range(i+1, m):
                if l[j] <= l[i]:
                    j = j - 1
                    break

            l[i], l[j] = l[j], l[i]

            l[i+1:] = l[i+1:][::-1]

    applySelections()

# papply(7, 4, print)
# papply([7,6,5,4,3,2], 4, print)
# papply([7,6,5,4,3,2], 4, print, sort = False)
# papply("7654321", 4, print)