class CircList:
    def __init__(self, size: int, default=0):
        self.data = [default] * size
        self.start = 0

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return CircListIter(self)

    def put(self, itm):
        self.data[self.start] = itm
        self.start = self._get_next()

    def _get_next(self, offset: int = 1):
        return (self.start + offset) % len(self.data)

    def _get_prev(self):
        if self.start == 0:
            return self.__len__() - 1
        return self.start - 1

    def get(self):
        return self.data[self._get_prev()]

    def get_at(self, offset):
        return self.data[self._get_next(offset)]

    def as_list(self):
        return [self.get_at(x) for x in range(self.__len__())]


class CircListIter:
    def __init__(self, data: CircList):
        self.data = data
        self.pos = -1

    # def __iter__(self):
    #    self.pos = -1
    #       return self

    def __next__(self):
        if self.pos < len(self.data) - 1:
            self.pos += 1
            return self.data.get_at(self.pos)
        else:
            raise StopIteration
