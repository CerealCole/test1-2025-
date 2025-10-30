""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 202x Test 1
"""
class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)


### DEFINE class VariableResistor HERE ###
class VariableResistor(Resistor):
    def __init__(self, res):
        super().__init__(res)          # sets self.resistance
        self._percentage = 100.0       # default 100%
        self.actual_resistance = res   # initialize actual_resistance

    def set_resistance(self, percent): # sets the actual resistance a percentage of the fixed resistance
        if percent < 0 or percent > 100:
            raise ValueError("Percentage must be between 0 and 100")
        self._percentage = percent
        self.actual_resistance = self.resistance * percent / 100

    def current(self, voltage): # return's the current with the actual resistance
        return voltage / self.actual_resistance

    def __str__(self): # return's as as string
        return "R=" + str(self.actual_resistance) + " (" + str(self._percentage) + "%)"


if __name__ == "__main__":
    r1 = Resistor(1000.0)
    print("R1: ", r1)
    print("R1: voltage = 12.0, current =", r1.current(12.0))

    ## UNCOMMENT THIS BLOCK TO TEST VariableResistor
    r2 = VariableResistor(1000.0)
    print("R2: ", r2)
    print("R2 100%: voltage = 12.0, current =", r2.current(12.0))
    r2.set_resistance(50.0)
    print("R2 50%: voltage = 12.0, current =", r2.current(12.0))
