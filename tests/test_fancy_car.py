"""
Test Script for Fancy Car Class

@author: Farshad Bolouri
"""

import pytest
from fancy_car import FancyCar

# Testing Constructor
def test_initial_values():
    car = FancyCar(True, True)
    assert car._engine == True and car._headlights == True and \
        car._maxSpeed == 100     # Accessing the Protected Members

def test_initial_values_2():
    car = FancyCar(True, False)
    assert car._engine == True and car._headlights == False and \
        car._maxSpeed == 100

def test_default_values():
        car = FancyCar() 
        assert car._engine == False and car._headlights == False and \
        car._maxSpeed == 100

def test_invalidInput(capfd):   # Checking for the Error Message in case of invalid input
    car = FancyCar("On", 5)
    out, err = capfd.readouterr()
    assert out == "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values.\n"

# Testing Getters and Setters 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def test_horn(capfd):
    car = FancyCar()
    car.horn()
    out, err = capfd.readouterr()
    assert out == "beep beep\n"    
#--------------------------------------------------------------------------
def test_gear_setter_drive():
    car = FancyCar(True, True)
    car.gear = "drive"                   # Not Capitalized
    assert car._gear == "Drive"          # Accessing the Protected Members

def test_gear_setter_reverse():
    car = FancyCar(True, True)
    car.gear = "Reverse"                 
    assert car._gear == "Reverse"        # Accessing the Protected Members

def test_gear_setter_wrongInput(capfd):  # Checking for the Error Message in case of invalid input
    car = FancyCar(True, True)
    car.gear = 78.5                      # Invalid Input
    out, err = capfd.readouterr()
    assert out == "Invalid input for Gear!\n" \
        "Only accepting String values.\n"
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# Testing using PyTest's Parametrization
@pytest.mark.parametrize("InputTime, Speed, Home, Odometer, Gear" \
    ", expectedHome, expectedOdometer", [
    (25, 35, 0, 0, "Drive",875, 875), 
    (5, 21, 0, 75, "Drive",105, 180),
    (32.3, 67, 2338, 0, "Reverse",173.9, 2164.1),
    (10.2, 0, 225, 225, "Drive",225, 225),
    (7, 25, 1245, 1993, "Reverse",1070, 2168),
    (15, 100, 644, 644, "Park", 2144, 2144)    
])

def test_drive(InputTime, Speed, Home, Odometer, Gear, \
    expectedHome, expectedOdometer):
    car = FancyCar(True, True)
    car.speed = Speed
    car.home = Home
    car.odometer = Odometer
    car.gear = Gear
    car.drive(InputTime)
    assert pytest.approx(car.home) == expectedHome and \
        pytest.approx(car.odometer == expectedOdometer)
#--------------------------------------------------------------------------
# Testing using PyTest's Parametrization
@pytest.mark.parametrize("InputTime, Speed, expectedSpeed", [
    (4, 0, 0),       # Full Stop
    (2, 45, 25),
    ("stop", 87, 0), # Full Stop Option Not Capitalized
    (3.5, 50, 15),
    (10, 45, 0),     # Full Stop
])

def test_brake(InputTime, Speed, expectedSpeed):
    car = FancyCar(True, True)
    car.speed = Speed
    car.brake(InputTime)
    assert car.speed == expectedSpeed
