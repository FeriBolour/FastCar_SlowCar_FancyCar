"""
Test Script for Slow Car Class

@author: Farshad Bolouri
"""

from slow_car import SlowCar

# Testing Constructor
def test_initial_values():
    car = SlowCar(True, True)
    assert car._engine == True and car._headlights == True and \
        car._maxSpeed == 37.5 and car._acceleration == 3.75 and \
            car._brakeEfficiency == -20     # Accessing the Protected Members

def test_initial_values_2():
    car = SlowCar(True, False)
    assert car._engine == True and car._headlights == False and \
        car._maxSpeed == 37.5 and car._acceleration == 3.75 and \
            car._brakeEfficiency == -20

def test_default_values():
        car = SlowCar() 
        assert car._engine == False and car._headlights == False and \
        car._maxSpeed == 37.5 and car._acceleration == 3.75 and \
            car._brakeEfficiency == -20


def test_invalidInput(capfd):   # Checking for the Error Message in case of invalid input
    car = SlowCar("On", 5)
    out, err = capfd.readouterr()
    assert out == "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values.\n"
