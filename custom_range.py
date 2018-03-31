#custom_range.py

class Range:
    
    def __init__(self, start, stop = None, step = 1):
        """Initialize a Range Instance"""
        if stop is None:
            start, stop = 0, start - 1
        if step == 0:
            raise ValueError("step cannot be zero!!!")

        # To make sure it is always upper-bound exclusive
        # For negative steps, add 1 to stop as it will be lower than start
        # subtract 1 for positive steps

        if step < 0 and start > stop:
            tn = stop + 1
        else:
            tn = stop

        # if start < stop for -ve step, The AP formula will yield a -ve value
        # for length, in that case, 0 becomes the length.
        # No need to raise an exception if start < stop for -ve step; since length
        # becomes zero, __getitem__ will raise an IndexError if an attempt is made
        # to access any item from the object
        
        self._length = max(0, (tn - start + step) // step)

        self._start, self._step = start, step

    def __len__(self):
        """Returns the number of items in the Range object"""
        return self._length

    def __getitem__(self, index):
        """Returns the item at a particular 'index' in the Range object"""

        # To support negative indices | k = -index; Range[k] = Range[len(Range) + k]
        if index < 0:
            index += len(self)

        # To make sure the index is between 0 and len(self)

        if not 0 <= index < len(self):
            raise IndexError("Index Out of Range!!!")

        return self._start + self._step * index   # AP formula | Tn = a +(n-1)d
        
    def __contains__(self, value):
        """Returns value in self"""
        # Reason for the 0 is same as above.
        # First, We find the index of value in Range. Logic is if the index is
        # a whole number, the value must be in Range. With the true div op,
        # if value is in Range, it should yield sth like 3.0 for index 3
        # if position is 0, it basically means the seq is empty,
        # if position - int(position) != 0, It is not a member of Range
        
        position = max(0, (value - self._start + self._step) / self._step)
        if position == 0 or position - int(position) != 0:
            return False
        else: return True
           
        
