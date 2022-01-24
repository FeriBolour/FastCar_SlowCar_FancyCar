"""
Test Script for Fast Car Class

@author: Farshad Bolouri
"""

from fast_car import FastCar

# Testing Constructor
def test_initial_values():
    car = FastCar(True, True)
    assert car._engine == True and car._headlights == True and \
        car._maxSpeed == 150 and car._acceleration == 10     # Accessing the Protected Members

def test_initial_values_2():
    car = FastCar(True, False)
    assert car._engine == True and car._headlights == False and \
        car._maxSpeed == 150 and car._acceleration == 10 

def test_default_values():
        car = FastCar() 
        assert car._engine == False and car._headlights == False and \
        car._maxSpeed == 150 and car._acceleration == 10 

def test_invalidInput(capfd):   # Checking for the Error Message in case of invalid input
    car = FastCar("On", 5)
    out, err = capfd.readouterr()
    assert out == "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values.\n"
