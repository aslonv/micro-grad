class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op
    
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
    
    def __sub__(self, other):
        out = Value(self.data - other.data, (self, other), '-')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out
    
a = Value(5.0)
b = Value(4.0)
c = Value(3.0)
# print(a + b) # python will call a.__add__(b)
# print(a - b) # python will call a.__sub__(b)
# print(a * b + c) # python will call a.__mul__(b) and then a.__add__(c)
d = a * b + c 
print(d._prev, d._op)