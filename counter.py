# *** Counter Class ***
class Counter(dict):
    def __getitem__(self, key):
        # Set Default Value
        return self.setdefault(key, 0)

    # Increment key in counter
    def increment(self, key):
        self.__setitem__(key, self.__getitem__(key) + 1)

    # Increment all keys in counter
    def incrementAll(self):
        for key in self.keys():
            self.__setitem__(key, self.__getitem__(key) + 1)

    # Reset key in counter
    def reset(self, key):
        self.__setitem__(key, 0)

    # Reset all keys in counter
    def resetAll(self):
        for key in self.keys():
            self.__setitem__(key, 0)

    # Returns a copy of itself
    def copy(self):
        return Counter(dict.copy(self))

    # Returns a list of keys sorted by their values
    def sortedKeys(self):
        return [x[0] for x in sorted(self.items(), key=lambda item: item[1])]

    # Returns a list of items sorted by their values
    def sortedItems(self):
        return [x for x in sorted(self.items(), key=lambda item: item[1])]

    # Returns the total count
    def total(self):
        return sum(self.values())
