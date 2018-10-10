from lang.T import T
from ast.Data import Mnist
from layer.Layer import Layer
from layer.CudaLayer import softmax, relu

K = 10
path = 'gen'

batchSize = 256
dim = [batchSize, 1, 28, 28]

learnRate = 0.005
momentum = 0.9
decay = 0.0005

trainIter = 10
testIter = 5


fc1 = Layer.full('fc1', 500)  # done
fc2 = Layer.full('fc2', K)  # done

network = softmax + fc2 + relu(2) + fc1  # done?

x = T._new('X', dim)  # done
y = T._new('Y', [batchSize])  # done

xCuda = x.asCuda  # done
yCuda = y.asIndicator(K).asCuda  # done

loss = (log_loss(yCuda) + network)(xCuda) # done?
accuracy = network(xCuda)

param = list(loss.freeParam)
solver = Train(trainIter, testIter, learnRate, momentum, decay, 0)

mnist = Mnist(dim)  # done
loop = Loop(loss, accuracy, mnist, (x, y), param, solver)

CudaCompile(path).compile(loop)
