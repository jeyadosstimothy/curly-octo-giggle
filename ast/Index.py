from derivation.IndexOp import IndexOp

class Index(IndexOp):
    def __add__(self, x):
        pass
    def __sub__(self, x):
        pass
    def __mul__(self, x):
        pass
    def __truediv__(self, x):
        pass
    def __mod__(self, x):
        pass
    def unflatten(self, flatDims):
        pass
    def grad(self, that):
        pass

class IndexDec(Index):
    def __init__(self, idx, dim):
        self.idx = idx
        self.dim = dim

    def sub(self, dl, dr):
        return IndexDec(self.idx, self.dim.sub(dl, dr))

class IndexVar:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def equals(self, that):
        pass
