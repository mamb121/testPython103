class A():
    def do_this(self):
        return "This is Class A"

class B(A):
    pass

class C():
    def do_this(self):
        return "This is Class C"

class D(B,C):
    pass

dd = D()
print(dd.do_this())
print(D.mro())