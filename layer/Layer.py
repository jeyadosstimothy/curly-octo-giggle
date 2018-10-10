from lang.T import *
from ast.Dim import *
from layer.Param import xavier, const
from ast.AExp import *

class Layer:
    def full(name, m2, weight=xavier, bias=const(0)):
        M1 = T.dim()
        M2 = DimConst(m2)
        w = T._new(weight.toInit(M1), name+'_W', M2, M1)
        b = T._new(bias.toInit(M1), name+'_B', M2, M1)

        N = T.dim()
        M2 = w.dim[0]
        M1 = w.dim[1]
        return T.fun(N, M1, lambda x: T.vec(N, M2, lambda i, j: T.sum(M1, lambda k: w.sub(j, k) * x.sub(i, k) + b.sub(j))))

    def log_loss(y_indicator):
        N = y_indicator.dim(0)
        K = y_indicator.dim(1)

        return T.fun(N, K, lambda x: (0 - T.sum(N, lambda i: T.sum(K, lambda k: y_indicator.sub(i, k) * Log(x.sub(i, k))))) / N.size)
