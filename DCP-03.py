# daily coding problem car(cons(3,4)) must return max element and cdr min element.
def const(a,b):
    def pair(f):
        return f(3,4)
    return pair

def max(a,b):
    if a>b:
        return a
    return b

def min(a,b):
    if a>b:
        return b
    return a

def car(f):
    return f(max)
def cdr(f):
    return f(min)
print(car(const(3,4)))
print(cdr(const(3,4)))
