from lang.T import T
from ast.Vec import FixVec
class CudaLayer:
    pass

class Activation(CudaLayer):
    pass

class Softmax(CudaLayer):
    pass

class ReLU(Activation):
    pass

softmax = T.fun(2, lambda x: FixVec(Softmax(), [x], x.dim))

def relu(n):
    return T.fun(n, lambda x: FixVec(ReLU(), [x], x.dim))
