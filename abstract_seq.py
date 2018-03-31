# abstract_seq.py

# My implementation of the abstract class "collections.Sequence" in the
# "collections" module

from abc import ABCMeta, abstractmethod


class Sequence(metaclass = ABCMeta):
    # This makes sure that a constructor declaration
    # for the Sequence class raises an error. No __init__ def
    @abstractmethod     # we do not provide an implementation but concrete classes MUST
    def __len__(self):
        """returns length of sequence"""

    @abstractmethod  # abstractmethod decorator syntax
    def __getitem__(self, index):
        """returns item at 'index' in sequence"""

    # concrete methods
    def __contains__(self, item):
        for i in range(len(self)):
            if self[i] == item:
                return True
        return False

    def __eq__(self, seq):
        if len(self) != len(seq):
            return False
        for i in range(len(self)):
            if self[i] != seq[i]: return False
        return True

    def __lt__(self, seq):
        if len(self) < len(seq): return True
        for i in range(len(self)):
            if self[i] < seq[i]: return True
        return False

    def count(self, item):
        count = 0
        for i in range(len(self)):
            if self[i] == item:
                count += 1
        return count

    def index(self, item):
        """returns the left-most index of 'item' in sequence"""
        for i in range(len(self)):
            if self[i] == item:
                return i
        else: raise ValueError(item + " not Found!!!!")
                
    
    
    
