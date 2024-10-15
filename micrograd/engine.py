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

    