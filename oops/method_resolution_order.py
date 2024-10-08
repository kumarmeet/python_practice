class A:
    pass


## single inheritance
class B(A):
    def show(self):
        print("B")


b = B()
b.show()
print(B.mro())


## multilevel inheritance
class C(B):
    def show(self):
        print("C")


c = C()
c.show()
print(C.mro())


class E:
    pass


class F:
    def show(self):
        print("F")


## multiple inheritance
class D(E, F):
    pass


d = D()
d.show()
print(D.mro())


class G:
    pass


class H(G):
    def show(self):
        print("H(G)")


class I:
    def again_show(self):
        print("I")


class J(I):
    pass


## hierarchical inheritance
class K(H, J, B):
    pass


k = K()

k.again_show()
k.show()

print(K.mro())
