class Data:
    def __init__(self):
        self.dim = []

    def load(self, option):
        return VecData(self, option)

class Mnist(Data):
    pass
