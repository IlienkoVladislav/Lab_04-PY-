class Buffer:
    """
    Class to buffer and process a sequence of numbers.

    Attributes:
        current_part: list to store the current part of the sequence

    Methods:
        __init__(self): constructor, initializes attributes
        add(self, *a): adds items to sequence and processes fives
        get_current_part(self): returns the current part of sequence
    """

    def __init__(self):
        """Constructor, initializes attributes."""
        self.current_part = []

    def add(self, *a):
        """
        Adds items to sequence and processes fives.

        Args:
            *a: items to add
        """
        self.current_part.extend(a)

        while len(self.current_part) >= 6:
            current_sum = sum(self.current_part[:5])
            print(f"Sum of five: {current_sum}")

            del self.current_part[:5]

    def get_current_part(self):
        """
        Returns the current part of sequence.

        Returns:
            List with items of the current part of sequence.
        """
        return self.current_part[:]

# Example usage:
buffer = Buffer()
buffer.add(2, 6, 8)
print(buffer.get_current_part())  
buffer.add(8, 10, 12)
print(buffer.get_current_part())  
buffer.add(14, 16, 18, 20)
print(buffer.get_current_part()) 
buffer.add(25)
print(buffer.get_current_part())  
