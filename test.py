class A():
    arr = []
    def __init__(self):
        self.arr = []

    def add(self, tmp):
        self.arr.append(tmp)


class B(A):
    # arr = []
    # def __init__(self):
    #     return self

    def add(self, tmp):
        super(B, self).add(tmp)
    

a = A()
a_1 = A()
# b = B()
a.add(1)
a_1.add(1)
# b.add(2)
# a.arr.append(1)
# b.arr.append(2)
print(a.arr)
# print(b.arr)
print(a_1.arr)