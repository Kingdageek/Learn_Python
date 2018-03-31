def check_index(key):
    """
        To check if index is negative or if its not an int. We're creating an
        infinite sequence
    """
    if key < 0: raise KeyError
    if not isinstance(key, int): raise TypeError


class ArithmeticSequence:
    
    def __init__(self, start= 0, step = 1):
        self.start = start
        self.step = step
        self.changed = {} #Empty dictionary to let us know if user has modified the sequence

    def __getitem__(self, key):
        check_index(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)

        self.changed[key] = value
        
