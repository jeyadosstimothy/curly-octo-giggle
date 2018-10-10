class Init:
    def __init__(self):
        self.fixed = False
        self.lr_mul = 1
        self.decay_mul = 1

class Caffe_Xavier(Init):
    def __init__(self, fan_in):
        self.fan_in = fan_in

    def sub(self, dl, dr):
        ret = Caffe_Xavier(self.fan_in.sub(dl, dr))
        ret.lr_mul = self.lr_mul
        ret.decay_mul = self.decay_mul
        ret.fixed = self.fixed
        return ret

class ConstInit(Init):
    def __init__(self, x):
        self.x = x

    def sub(self, dl, dr):
        return self
