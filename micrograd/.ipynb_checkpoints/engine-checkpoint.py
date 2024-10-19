class Value:
    """
    Stores a single scalar value and its gradient
    """
    def __init__(self, data, _children(), _op=''):
        self.data = data
        self.grad = 0
        # Internal variables used for autograd graph construction
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op # The op that produced this node, for graphviz / debugging / etc

    def __repr__(self):
        return f"Value(data=(self.data))"
    
    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out 
    
a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a*b + c