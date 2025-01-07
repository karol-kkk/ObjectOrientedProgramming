class C:
    def __init__(self, sectors):
        """Initializes the stadium with the given sectors and their respective fan counts."""
        self.sectors = sectors

    def m1(self, s, n):
        """Changes the number of fans in sector s, or adds a new sector with n fans."""
        self.sectors[s] = n

    def m2(self, s):
        """Returns the sum of fans in the sectors listed in string s."""
        return sum(self.sectors[sector] for sector in s if sector in self.sectors)


# Example usage:

# Creating a stadium with initial data
stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

# Using m1 to modify a sector's fans or add a new sector
stadium.m1("G", 130)

# Using m2 to calculate the sum of fans in the specified sectors
print(stadium.m2("GD"))  # Output: 280
print(stadium.m2("KEJ"))  # Output: 110
