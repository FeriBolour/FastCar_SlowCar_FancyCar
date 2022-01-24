"""
Test Script for Base Car Class

@author: Farshad Bolouri
"""

import pytest
from base_car import BaseCar

# Testing Constructor
def test_initial_values():
    car = BaseCar(True, True)
    assert car._engine == True and car._headlights == True  # Accessing the Protected Members

def test_initial_values_2():
    car = BaseCar(True, False)
    assert car._engine == True and car._headlights == False

def test_default_values():
        car = BaseCar() 
        assert car._engine == False and car._headlights == False

def test_invalidInput(capfd):   # Checking for the Error Message in case of invalid input
    car = BaseCar("On", 5)
    out, err = capfd.readouterr()
    assert out == "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values.\n"
# Testing Getters and Setters 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def test_engine_getter_True():
    car = BaseCar(True, True)
    assert car.engine == True    

def test_engine_getter_False():
    car = BaseCar()
    assert car.engine == False

def test_engine_setter_True():
    car = BaseCar()
    car.engine = False
    assert car._engine == False             # Accessing the Protected Members

def test_engine_setter_False():
    car = BaseCar()
    car.engine = False
    assert car._engine == False

def test_engine_setter_wrongInput(capfd):   # Checking for the Error Message in case of invalid input
    car = BaseCar()
    car.engine = "On"
    out, err = capfd.readouterr()
    assert out == "Invalid input for Engine!\nOnly accepting Boolean values.\n"

#--------------------------------------------------------------------------
def test_headlights_getter_True():
    car = BaseCar(True, True)
    assert car.headlights == True

def test_headlights_getter_False():
    car = BaseCar()
    assert car.headlights == False

def test_headlights_setter_True():
    car = BaseCar()
    car.headlights = False
    assert car._headlights == False         # Accessing the Protected Members

def test_headlights_setter_False():
    car = BaseCar()
    car.headlights = False
    assert car._headlights == False

def test_headlights_setter_wrongInput(capfd):   # Checking for the Error Message in case of invalid input
    car = BaseCar()
    car.headlights = "Off"
    out, err = capfd.readouterr()
    assert out == "Invalid input for headlights!\nOnly accepting Boolean values.\n"
#--------------------------------------------------------------------------
def test_speed_getter():
    car = BaseCar()
    car._speed = 55                         # Accessing the Protected Members
    assert car.speed == 55

def test_speed_setter():
    car = BaseCar(True, True)
    car.speed = 45
    assert car._speed == 45                 # Accessing the Protected Members
   
def test_speed_setter_wrongInput(capfd):    # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.speed = "Fast"
    out, err = capfd.readouterr()
    assert out == "Invalid input for speed!\nOnly accepting Float or Integer values.\n"
#--------------------------------------------------------------------------
def test_odometer_getter():
    car = BaseCar()
    car._odometer = 87.78                   # Accessing the Protected Members
    assert car.odometer == 87.78

def test_odometer_setter():
    car = BaseCar(True, True)
    car.odometer = 99
    assert car._odometer == 99             # Accessing the Protected Members

def test_odometer_setter_wrongInput(capfd):    # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.odometer = "No Way Home!"
    out, err = capfd.readouterr()
    assert out == "Invalid input for odometer!\nOnly accepting Float or Integer values.\n"
#--------------------------------------------------------------------------
def test_home_getter():
    car = BaseCar()
    car._home = 45.5                       # Accessing the Protected Members
    assert car.home == 45.5

def test_home_setter():
    car = BaseCar(True, True)
    car.home = 34526.5
    assert car._home == 34526.5            # Accessing the Protected Members

def test_home_setter_wrongInput(capfd):    # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.home = "Far From Home!"
    out, err = capfd.readouterr()
    assert out == "Invalid input for Distance From Home!\nOnly accepting Float or Integer values.\n"
#--------------------------------------------------------------------------
def test_gear_getter():
    car = BaseCar()
    car._gear = "Park"                     # Accessing the Protected Members
    assert car.gear == "Park"

def test_gear_setter():
    car = BaseCar(True, True)
    car.gear = "drive"                   # Not Capitalized
    assert car._gear == "Drive"          # Accessing the Protected Members


def test_gear_setter_moving(capfd):      # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.gear = 'Drive'
    car.speed = 15
    car.gear = 'Park'
    out, err = capfd.readouterr()
    assert out == "Can't change gears while still moving!\n" \
        "Current Speed = 15 m/s\n" \
            "--------------------------------------------------------------\n"

def test_gear_setter_wrongGear(capfd):   # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.gear = "Sport"                   # Invalid Input
    out, err = capfd.readouterr()
    assert out == "This gear does not exist!\n" \
            "--------------------------------------------------------------\n"

def test_gear_setter_wrongInput(capfd):  # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.gear = 65.5                      # Invalid Input
    out, err = capfd.readouterr()
    assert out == "Invalid input for Gear!\n" \
        "Only accepting String values.\n"
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def test_on():
    car = BaseCar()
    car.on()
    assert car._engine == True and car._home == 0          # Accessing the Protected Members
#--------------------------------------------------------------------------
def test_off():
    car = BaseCar(True, True)
    car.off()
    assert car._engine == False         # Accessing the Protected Members
#--------------------------------------------------------------------------
# Testing using PyTest's Parametrization
@pytest.mark.parametrize("InputTime, Speed, expectedSpeed", [
    (5, 0, 25),
    (12.5, 45, 50),  # Max Speed Reached
    (2.78, 5, 18.9),
    (8, 3.5, 43.5),
    (20, 7, 50),     # Max Speed Reached
])

def test_gas(InputTime, Speed, expectedSpeed):
    car = BaseCar(True, True)
    car.speed = Speed
    car.gas(InputTime)
    assert car.speed == expectedSpeed

def test_gas_wrongInput(capfd):  # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.gas("A Lot")                      # Invalid Input
    out, err = capfd.readouterr()
    assert out == "Invalid input for Gas Time!\nOnly accepting Float or Integer values.\n"
#--------------------------------------------------------------------------
# Testing using PyTest's Parametrization
@pytest.mark.parametrize("InputTime, Speed, Home, Odometer, expectedHome" \
    ", expectedOdometer", [
    (25, 35, 0, 0, 875, 875), 
    (5, 21, 0, 75, 105, 180),
    (32.3, 67, 2338, 0, 4502.1, 2164.1),
    (10.2, 0, 225, 225, 225, 225),
    (7, 25, 1245, 1993, 1420, 2168),    
])

def test_drive(InputTime, Speed, Home, Odometer, expectedHome, expectedOdometer):
    car = BaseCar(True, True)
    car.speed = Speed
    car.home = Home
    car.odometer = Odometer
    car.drive(InputTime)
    assert car.home == expectedHome and car.odometer == expectedOdometer

def test_drive_wrongInput(capfd):  # Checking for the Error Message in case of invalid input
    car = BaseCar(True, True)
    car.drive("Fast")                      # Invalid Input
    out, err = capfd.readouterr()
    assert out == "Invalid input for Drive Time!\nOnly accepting Float or Integer values.\n"
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
    car = BaseCar(True, True)
    car.speed = Speed
    car.brake(InputTime)
    assert car.speed == expectedSpeed
