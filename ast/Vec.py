from derivation.VecOp import *
from ast.Dim import *

class Vec(VecOp):
    def __add__(self, v):
        pass
    def __mul__(self, v):
        pass
    def convolv(self, w):
        pass
    def clip(self, bound):
        pass
    def __len__(self):
        pass
    def apply(self, i):
        pass
    def of(self, i):
        pass
    def grad(self, x):
        pass

class VecDec(Vec):
    def __init__(self, v, dim):
        self.v = v
        self.dim = dim

    def __repr__(self):
        return str(self.v)

    def _free(self):
        return Set(self)

    def assign(self, rhs): # <-- operator
        pass

    def getIndices(self):
        pass

    def getDims(self):
        return self.dim

    def get(self, i):
        pass

    def free(self, i):
        return False

    def contains(self, v):
        if self == v:
            return True
        else:
            return False
    def asCuda(self):
        return CudaVec(self)

    def asIndicator(self, k):
        if type(k) is int:
            k = DimConst(k)
        return VecAsIndicator(self, k)

    def sub(self, dl, dr):
        return VecDec(self.v, list(map(lambda dx: dx.sub(dl, dr), self.dim)))

class CudaVec(VecDec):
    def __init__(self, vec):
        self.vec = vec # copy()

    def __repr__(self):
        return "Cuda(%s)" % self.vec

    def _free(self):
        return set()

    def contains(self, v):
        return self.vec.contains(v)

    def sub(self, dl, dr):
        return CudaVec(self.vec.sub(dl, dr))


class VecAsIndicator(VecDec):
    def __init__(self, vec, numOfCls):
        self.vec = vec.copy() # copy()
        self.numOfCls = numOfCls

    def __repr__(self):
        return "Indicator(%s, %s)" % self.vec, self.numOfCls

    def _free(self):
        return set()

    def contains(self, v):
        return self.vec.contains(v)

    def sub(self, dl, dr):
        return VecAsIndicator(self.vec.sub(dl, dr), self.numOfCls)

class VecExp(Vec):
    def __init__(indices, e):
        self.indices = indices
        self.e = e

    def equals(self, that):
        pass

class VecVar:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, x):
        pass

class VecParam(VecDec):
    def __init__(self, init, v, dim):
        self.init = init
        self.v = v
        self.dim = dim

    def _free(self):
        return set(self)

    def sub(self, dl, dr):
        return VecParam(self.init.sub(dl, dr), self.v, list(map(lambda d: d.sub(dl, dr), self.dim)))

    def update(self, dv):
        return Update(self, dv)


class FixVec(Vec):
    def __init__(self, layer, param, dim):
        self.layer = layer
        self.param = param
        self.dim = dim

    def sub(self, dl, dr):
        self._sub(dl, dr)

    def _sub(l, r):
        if type(l) is Vec:
            return FixVec(self.layer, list(map(lambda p: p.sub(l, r), self.param)), self.dim)
        elif type(l) is Dim:
            return FixVec(self.layer, list(map(lambda p: p.sub(l, r), self.param)), list(map(lambda d: d.sub(l, r), self.dim)))

