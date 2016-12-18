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
    return Dual_number(x)
        
