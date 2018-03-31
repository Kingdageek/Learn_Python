# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:36:15 2017

@author: WIZZY

On Tue Jul 12 'some radical time' 2017, I MADE THE CODE MORE PYTHONIC
LIST COMPREHENSIONS, ZIP, A CLASS METHOD, DECORATOR.

"""

# multidim_vector.py


class Vector: 
    """Represent a Vector in n-dimensional space. Supports basic Vector 
    operations"""
    
    def __init__(self, *dim):
        """
        initialize vector object with 'dim' number of coordinates
        if 'dim' is an integer.
        
        If 'dim' contains a single float or contains 2 or more numbers,
        initialize the vector
        with the numbers as coordinate values
        
        I actually think this is highly unnecessary though, like i
        should remove the __setitem__. :)
        
        """
        if len(dim) == 1 and isinstance(dim[0], int):
            self._coords = [0] * dim[0]
        else:
            self._coords = list(dim)
    
    @classmethod
    def fromlist(cls, l):
        """Return an instance of 'Vector' from a list 'l'"""
        
        if not isinstance(l, list):
            raise TypeError()
        instance = cls()
        instance._coords = l
        return instance            
        
    def __len__(self):
        return len(self._coords)
    
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Must be set to an int or a float!")
        else:
            self._coords[index] = value
                        
    def __getitem__(self, index):
        return self._coords[index]
        
    def __add__(self, other):
        if len(other) > len(self):
            raise ValueError("Must be of the same Length!")
        #result = Vector(len(self))
        result = [i + j for i, j in zip(self._coords,other._coords)]                
        return Vector.fromlist(result)
    
    def __sub__(self, other):
        if len(other) > len(self):
            raise ValueError("Must be of the same Length!")
        result = [i - j for i, j in zip(self._coords, other._coords)]
        return Vector.fromlist(result)

    def __neg__(self):
        """Returns the vector with every element negated"""
        result = [-i for i in self._coords]
        return Vector.fromlist(result)

    def __mul__(self, value):
        """Scalar Multiplication for Vector
           
           value: an int or a Vector. 
           
           result: a scalar obtained by term by term multiplication if 'value'
                   is a Vector or by a 'value(Vector)' if 'value' is 'int'
        """
        if isinstance(value, Vector) and len(self) == len(value):
            result = [i * j for i, j in zip(self._coords, value._coords)]
            result = sum(result)
        elif isinstance(value, Vector) and len(self) != len(value):
            raise ValueError("Vector Must be of the same length!")                
        elif not isinstance(value, (int, float)):
            raise TypeError("Must Multiply with an int or a float! | " 
                            + value.__class__.__name__ + " supplied")
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] += self[j] * value
        return result   
    
    __rmul__ = __mul__
            
    def __eq__(self,other):
        """return True if Vector has the same coordinates as 'other'"""
        return self._coords == other._coords    
    
    def __ne__(self,other):
        return not (self == other)
    
    def __str__(self):
        """To return a string representation of Vector"""
        middle = str(self._coords)[1:-1]        
        return "<" + middle + ">"    
    
    def __repr__(self):
        """How Vector should look as python code"""
        args = ", ".join(repr(i) for i in self._coords)
        return "<{}>".format(args)    
    
    def magnitude(self):
        """
            returns the magnitude of the Vector
        """
        result = [i ** 2 for i in self._coords]
        result = round(sum(result) ** 0.5, 2)
        return result    
    
    def unit_vector(self):
        """
            returns unit vector in the direction of Vector
        """    
        magnitude = self.magnitude()
        result = [round(i / magnitude, 2) for i in self._coords]
        return Vector.fromlist(result)
    
def test():
    import doctest
    doctest.testmod()
    
test()
        
