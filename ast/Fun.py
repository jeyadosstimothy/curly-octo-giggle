class Vec2ScalarFun:
    def __init__(param, body):
        self.param = param
        self.body = body

    def apply(self, v):
        pass

    def grad(self, v=None):
        pass

    def __add__(self, fun):
        pass

    def sub(l, r):
        pass

    def contains(self, v):
        pass

    def free(self, i):
        pass

    def equals(self, that):
        pass

class VecFun:
    def __init__(self, param, body):
        self.param = param
        self.body = body

    def apply(self, v):
        pass

    def grad(self, v=None):
        pass

    def __add__(self, fun):
        pass

    def sub(l, r):
        pass

    def contains(self, v):
        pass

    def free(self, i):
        pass

    def equals(self, that):
        pass
