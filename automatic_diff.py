# dual numbers class
import math
class Dual_number:
    """Dual numbers API"""
    def __init__(self, _real, _dual=0):
        self.real = _real
        self.dual = _dual
    
    # present a number to the world:
    def __str__(self):
        def sign_help(x):
            return '+' if self.dual >= 0 else '-' 
        return str(self.real) + ' ' + sign_help(self.dual) + ' ' + str(abs(self.dual)) + 'e'
    
    def __add__(self, other):
        if not isinstance(other, Dual_number):
            other = dual_number(other)
            return Dual_number(self.real + other.real, self.dual + other.dual)
        else:
            return Dual_number(self.real + other.real, self.dual + other.dual)
    
    def __radd__(self, other):
        return Dual_number(self.real + other, self.dual)
    
    def __sub__(self, other):
        if not isinstance(other, Dual_number):
            other = dual_number(other)
            return Dual_number(self.real - other.real, self.dual - other.dual)
        else:
            return Dual_number(self.real - other.real, self.dual - other.dual)
    
    def __rsub__(self, other):
        return Dual_number(-(self.real - other), -self.dual)
    
    def __mul__(self, other):
        if not isinstance(other, Dual_number):
            other = dual_number(other)
            return Dual_number(self.real * other.real, self.real * other.dual + 
                          self.dual * other.real)
        else:
            return Dual_number(self.real * other.real, self.real * other.dual + 
                          self.dual * other.real)
    
    def __rmul__(self, other):
        return Dual_number(self.real * other, self.dual * other)
    
    def __truediv__(self, other):
        if not isinstance(other, Dual_number):
            other = dual_number(other)
            return Dual_number(self.real / other.real ,  (self.dual * other.real - 
                                                     self.real * other.dual) / (other.real * other.real))
        else:
            return Dual_number(self.real / other.real ,  (self.dual * other.real - 
                                                     self.real * other.dual) / (other.real * other.real))
    def __rtruediv__(self, other):
        return Dual_number((1 / self.real) * other, ((-1 * self.dual) / self.real * self.real) * other )
    
def dual_number(x):
    """converse tu dual number x + 0e"""
    return Dual_number(x)
# few functions, call math with real argument:
def sin(x):
    if isinstance(x, Dual_number):
        return Dual_number(math.sin(x.real), x.dual * math.cos(x.real))
    else:
        return math.sin(x)
    
def cos(x):
    if isinstance(x, Dual_number):
        return Dual_number(math.cos(x.real), -x.dual * math.sin(x.real))
    else:
        return math.sin(x)

def tan(x):
    """tangent x for |x|  < pi / 2 """
    if isinstance(x, Dual_number):
        return sin(x) / cos(x)
    else:
        return math.tan(x)
    
def cot(x):
    if isinstance(x, Dual_number):
        return cos(x) / sin(x)
    else:
        return math.cos(x) / math.sin(x)

def sinh(x):
    if isinstance(x, Dual_number):
        return  Dual_number(math.sinh(x.real), x.dual * math.cosh(x.real))
    else:
        return math.sinh(x)

def cosh(x):
    if isinstance(x, Dual_number):
        return Dual_number(math.cosh(x.real), -x.dual * math.sinh(x.real))
    else:
        return math.cosh(x)

def tanh(x):
    if isinstance(x, Dual_number):
        return sinh(x) / cosh(x)
    else:
        return math.tanh(x)

def coth(x):
    """coth if x or x.real not eq to 0"""
    if isinstance(x, Dual_number):
        return cosh(x) / sinh(x)
    else:
        return math.cosh(x) / math.sinh(x)
        
def sqrt(x):
    if isinstance(x, Dual_number):
        return Dual_number(math.sqrt(x.real), (x.dual) / (2 * sqrt(x.real)))
    else:
        return math.sqrt(x)
def cube_root(x):
    if isinstance(x, Dual_number):
        return Dual_number(x.real ** (1/3), (x.dual) / (3 * (x.real ** 2)**(1 / 3)))
    else:
        return x ** (1 / 3)

def exp(x):
    if isinstance(x, Dual_number):
        return Dual_number(math.exp(x.real), math.exp(x.real) * x.dual)
    else:
        return math.exp(x)
    
def ln(x):
    if isinstance(x, Dual_number):
        if not x.dual is 0:
            return Dual_number(math.log(x.real) ,  (x.real / x.dual))
        else:
            return Dual_number(math.log(x.real))
    else:
        return math.log(x)


def pow(a, x):
    if isinstance(x, Dual_number):
        if not x.dual is 0:
            return Dual_number(math.pow(a, x.real), math.pow(a, x.real) * x.dual * ln(x.dual))
        else:
            return Dual_number(math.pow(a, x.real))
    else:
        return math.pow(a, x)
        
