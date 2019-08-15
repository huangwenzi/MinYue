class A():
    arr = []
    def __init__(self):
        self.arr = []

    @staticmethod
    def add(self, tmp):
        self.arr.append(tmp)


class B(A):

    def add(self, tmp):
        super(B, self).add(tmp)
    
a = A()
a_1 = A()
a.add(a, 1)
print(a.arr)
print(a_1.arr)