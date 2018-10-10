from ast.Init import *

class ParamInit:
    pass

class XavierParam(ParamInit):
    pass

class ConstParam(ParamInit):
    def __init__(self, x):
        self.x = x

class Param:
    def __init__(self, init, lr_mul, decay_mul, isFixed):
        self.init = init
        self.lr_mul = lr_mul
        self.decay_mul = decay_mul
        self.isFixed = isFixed

    def toInit(self, fan_in):
        ret = None
        if self.init is XavierParam:
            ret = Caffe_Xavier(fan_in)
        elif type(self.init) is ConstParam:
            ret = ConstInit(self.init.x)
        ret.lr_mul = self.lr_mul
        ret.decay_mul = self.decay_mul
        ret.fixed = self.isFixed
        return ret

xavier = Param(XavierParam, 1, 1, False)

def const(x, lr_mul=1, decay_mul=1):
    return Param(ConstParam(x), lr_mul, decay_mul, False)
