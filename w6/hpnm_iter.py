class hpapply:

    def __init__(self, data, m):

        # verify data is integer, string or list
        self.m = m
        self.l = [0] * (m - 1) + [-1]
        if isinstance(data, int):
            self.n = data
            self.data = list(range(data))
        elif isinstance(data, str) or isinstance(data, list):
            self.n = len(data)
            self.data = data
        else:
            raise Exception("Unsupported data type {}".format(type(data)))

    def __iter__(self):
        return self

    def __next__(self):

        self.l[self.m - 1] += 1

        for i in reversed(range(self.m)):
            if self.l[i] == self.n:
                self.l[i] = 0
                if i != 0:
                    self.l[i - 1] += 1
                else:
                    raise StopIteration()

        return [self.data[i] for i in self.l]

# for i in hpapply("456", 3):
#     print(i)