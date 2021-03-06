class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, new_item):
        """
        Attempts to add an item to the list of items in this bin.
        """
        if self.can_add_item(new_item):
            self.items.append(new_item)
            return True
        return False

    def can_add_item(self, new_item):
        """
        Determines whether the specified item can be added to the bin's list of items.
        """
        return new_item.size <= self.open_space()

    def filled_space(self):
        """
        Gets the amount of space currently in use by items in the bin.
        """
        return sum(item.size for item in self.items)

    def open_space(self):
        """
        Gets the amount of space that is still available in this bin.
        """
        return self.capacity - self.filled_space()

    def fitness(self):
        """
        Returns a value that can be used to indicate the fitness of this bin when calculating the fitness of a solution.
        """
        return (self.filled_space() / self.capacity) ** 2
