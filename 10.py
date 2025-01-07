class C:
    def __init__(self, coordinates):
        """Initializes the object with a list of coordinates."""
        self.coordinates = coordinates

    def m(self, n):
        """Returns True if there are at least n points in the first quadrant."""
        # Count how many points are in the first quadrant (both x and y > 0)
        count = 0
        for point in self.coordinates:
            if point[0] > 0 and point[1] > 0:
                count += 1
        
        # Return True if there are at least n points in the first quadrant
        return count >= n


# Example usage:

# Creating an object with a list of coordinates
obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

# Testing the m(n) method
print(obj.m(2))  # Output: True
print(obj.m(3))  # Output: False
