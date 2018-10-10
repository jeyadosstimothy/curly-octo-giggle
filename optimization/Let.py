class Let:
    pass

class Update(Let):
    def __init__(self, x, v):
        self.x = x
        self.v = v

    def __repr__(self):
        return '%s = %s' % self.x, self.v
    def sub(self, vl, vr):
        return Update(self.x, self.v.sub(vl, vr))

    def contains(y):
        return self.v.contains(y)
