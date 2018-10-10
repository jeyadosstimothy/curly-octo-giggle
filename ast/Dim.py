class Dim:
    def __len__(self):
        pass
    def __mul__(self, x):
        pass
    def __truediv__(self, x):
        pass
    def __sub__(self, x):
        pass
    def __add__(self, x):
        pass


class DimConst(Dim):
    def __init__(self, bound):
        self.bound = bound

    def __repr__(self):
        return str(self.bound)

    def sub(self, dl, dr):
        return self

class DimVar(Dim):
    def __init__(self, name):
        self.name = name

    def equals(self, that):
        pass

    def sub(self, dl, dr):
        if self == dl:
            return dr
        else:
            return self
