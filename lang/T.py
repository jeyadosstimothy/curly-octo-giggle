from ast.Vec import *
from ast.Init import *
from ast.Index import *
from ast.AExp import *
from ast.Fun import *

class T:
    vec_count = 0

    @staticmethod
    def _new(*params):
        print("T.py", "_new", params)
        if issubclass(type(params[0]), Init):
            init = params[0]
            name = params[1]
            dims = []
            if type(params[2]) is tuple or type(params[2]) is list:
                dims = params[2]
            else:
                dims = params[2:]
            return VecParam(init, VecVar(name), dims)
        elif type(params[0]) is str:
            name = params[0]
            dims = []
            if type(params[1]) is tuple or type(params[1]) is list:
                dims = params[1]
            else:
                dims = params[1:]
            if type(dims[0]) is int:
                dims = list(map(lambda x: T.dim(x), dims))
            return VecDec(VecVar(name), dims)
        elif issubclass(type(params[0]), Dim):
            T.vec_count+=1
            dim = params
            return VecDec(VecVar("X"+ str(T.vec_count)), dim)
        elif (type(params[0]) is list  or type(params[0]) is tuple):
            return T._new(*params[0])
        elif type(params[0]) is int:
            assert len(params) == 1
            n = params[0]
            return T._new(list(map(T.dim, range(1, n+1))))


    dim_count=0

    @staticmethod
    def dim(n=None):
        if n is None:
            T.dim_count+=1
            return DimVar("N" + str(T.dim_count))
        return DimConst(n)

    @staticmethod
    def vec(*params):
        print('T.py', 'in vec', params)
        f = params[-1]
        d = params[:-1]
        return T.vec_app(d, lambda i: f(*i))

    def vec_app(d, f):
        i = list(map(lambda dim: T.index(dim), d))
        return VecExp(i, f(i))

    index_count = 0

    @staticmethod
    def index(*params):
        if len(params)==1:
            dim = params[0]
            T.index_count+=1
            return IndexDec(IndexVar('i' + str(T.index_count)), dim)
        else:
            name = params[0]
            dim = params[1]
            return IndexDec(IndexVar(name), dim)

    @staticmethod
    def sum(*params):
        print('T.py', 'in sum', params)
        f = params[-1]
        d = params[:-1]
        return T.sum_app(d, lambda i: f(*i))

    def sum_app(d, f):
        i = list(map(lambda dim: T.index(dim), d))
        e = f(i)
        for c in reversed(i):
            e = Sum(e, c)
        return e

    @staticmethod
    def fun(*params):
        print('T.py', 'in fun', params)
        f = params[-1]
        d = params[:-1]

        print(d)
        x = T._new(d)
        temp = f(x)
        if issubclass(type(temp), AExp):
            print('T.py', 'Vec2ScalarFun')
            return Vec2ScalarFun(s, f(x))
        else:
            print('T.py', 'VecFun')
            return VecFun(x, f(x))
