from derivation.AExpOp import *


class AExp(AExpOp):
    def grad(self, v):
        return Gradient(self, v)


class Sum(AExp):
    def __init__(self, i, e):
        self.i = i
        self.e = e

class Log(AExp):
    def __init__(self, e):
        self.e = e
