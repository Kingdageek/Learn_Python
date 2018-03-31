#Progressionc.py
"""Defined classes for a variety of progressions.

A base class called 'Progression' that other classes inherit
"""

class Progression:
    
    def __init__(self, start= 0):
        """
        Generic progression class, Sequence is made up of
        whole numbers
        """
        self._current = start

    def _advance(self):
        """nonpublic method to determine next element of the
        Progression. In this case, 0,1,2,3...

        Subclasses to override this method to customize the
        kind of progressions they display
        """
        self._current += 1

    # Iterator methods
    def __next__(self):
        """return next element in progression and maintain its
        position in the progression. Raises a StopIteration Error
        if no more elements in <finite> progression
        """
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current # hold prev value of _current
            self._advance() # update _current to next value in the
                            #progression
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        """Outputs the first 'n' values of Progression"""
        print(" ".join(str(next(self)) for i in range(n)))


class ArithmeticProgression(Progression):
    
    def __init__(self, increment = 1, start = 0):
        super().__init__(start)
        self._increment = increment

    # Overriding the _advance method.
    def _advance(self):
        """
        The AP progresses by adding a fixed value to the preceding
        value
        """
        self._current += self._increment  # Accessing the superclass's field


class GeometricProgression(Progression):
    
    def __init__(self, base = 2, start= 1):
        """started at 1 to avoid always getting zero"""
        super().__init__(start)
        self._base = base

    # Overriding the _advance method. Customizing it to suit this progress
    def _advance(self):
        self._current *= self._base

    
class FibonacciProgression(Progression):
    
    def __init__(self, first = 0, second = 1):
        super().__init__(first)  # the superclass's self._current becomes
                                 # the first value
        self._prev = second - first  # value preceding the first value

    # Overriding the _advance method to produce fibonacci numbers.
    def _advance(self):
        """In superclass's __next__ method, self._current is reported before
        _advance is invoked to update it; So, in this class, the first value
        passed to the constructor is reported first as self._current before
        the logic that's in this _advance overriden method is invoked
        """
        self._prev, self._current = self._current, self._prev + self._current
        

class AbsoluteProgression(Progression):

    def __init__(self, first= 2, second = 200):
        super().__init__(first)         # would assign first to self._current
        self._prev = first + second

    def _advance(self):
        """Each value is the absolute value of the difference between the
        two previous values
        """
        self._prev, self._current = self._current, abs(self._prev - self._current)
        

class SquareRootProgression(Progression):

    def __init__(self, start = 65536):
        super().__init__(start)

    def _advance(self):
        """Each value is the square of the previous value"""
        from math import sqrt
        self._current = sqrt(self._current)

    def print_progression(self, n):
        """Outputs the first 'n' values of Progression. Overridden version
        To suit SquareRootProgression
        """
        print(" ".join(str(round(next(self), 5)) for i in range(n)))
        
