"""
Fast Car Class

@author: Farshad Bolouri
"""

from base_car import BaseCar


class FastCar(BaseCar):
    
    # constructor
    def __init__(self, engine = False, headlights = False):
        try:
            assert isinstance(engine, bool) and isinstance(headlights, bool)  \
                , "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values."
            super().__init__(engine, headlights)
            #Fast Car Features
            self._maxSpeed = 3 * self._maxSpeed
            self._acceleration = 2 * self._acceleration
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------
    # Overriding the stats function from base class
    def stats(self):
        print("--------------------------------------------------------------")
        print("                    FastCar's Dashboard                      ")
        super().stats()
