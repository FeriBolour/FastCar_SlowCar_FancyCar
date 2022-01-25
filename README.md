# One Car, Two Car, Fast Car, Slow Car

__Details__

You are assigned to design 3 different cars: _FastCar_, _SlowCar_, and _FancyCar_.

Each of these cars share basic functionality that all average cars have (listed below), but they sadly cannot turn.
They travel on the Infinitely Long Road (ILR), a straight road with no wind resistance that goes on forever in both directions.
All cars have the stats of an average car unless otherwise stated.

Multiple cars can be driving at the same time, each on their own ILR (don't worry about collisions)

__Problem Statement__

On the ILR, you have one of each of the 3 different cars (_FastCar_, _SlowCar_, and _FancyCar_).  In the `main` race between them here is what happens.

1. All three cars start their engines
2. `FastCar` and `FancyCar` turn on their lights
3. All three cars gas for 11 seconds
4. All three cars drive for 30 seconds
5. `FancyCar` brakes for 5 seconds, slowing down in order to enjoy the scenery around it, then continues driving for 3 seconds
6. `SlowCar` brakes for 6 seconds, curious what `FancyCar` is looking at
7. `FancyCar` realizes they left their lucky keychain behind and immediately brakes to a full stop, changes to reverse, gases for 20 seconds, then drives for an additional 30 seconds
8. After realizing headlights aren't that useful while going in reverse, `FancyCar` turns off its lights
9. `FastCar`, all the while, continues driving for another 30 seconds, gasses 20 seconds, and drives an addition 60 seconds
10. `SlowCar` feels lonely (now that both cars have left it behind), comes to a full stop, then turns off its engine
11. All three cars check their dashboards
12. `FancyCar` honks its horn twice, celebrating that it found its lost keychain

---
## Average Car
### Average Car stats

- Max Speed: 50 meters/sec
  - Any acceleration cannot make the car go faster than its max
- Acceleration: 5 meters/sec^2
  - If the car is accelerating forward, it is this value. Gas pedal acts as a binary switch
- Brake efficiency: -10 meters/sec^2
  - If the car is braking, it is this value. Brake pedal acts as a binary switch

### Average Car Features

1. turn on
   - turns on engine (allows for gas, driving, and braking to take affect)
   - establishing starting point ('home') on the ILR
2. turn off
   - turns off engine (disallows gas, driving, and braking)
   - engine cannot turn off while car is still moving (speed must be 0)
3. gas
   - adds gas to the engine, accelerates the car
   - Accelerates the car depending on how long the gas pedal is pressed (in secs)
   - Should accept a time value for how long the pedal is pressed to accelerate
   - should not affect distance, only affects speed
4. drive
   - continues driving in same direction
   - should accept a time value for how long to continue driving (in secs)
   - no change in acceleration (These cars should assume there is no natural deceleration, if the car is driving, then it is coasting at a steady speed)
   - average cars can only move forward
5. brake
   - slows down the vehicle
   - Should accept a time value for how long the pedal is pressed to brake (in secs)
   - should not affect distance, only affects speed
6. headlights
   - can turn on or off despite if the engine is on/off
7. check dashboard
   - should show current car stats:
     - engine on/off
     - headlights on/off
     - current speed
     - odometer:
       - distance traveled in trip
     - home:
       - distance from 'home'
     - current gear (direction car is moving)
       - park: when speed is 0
       - drive: moving forward
       - reverse: moving backward
---

## Unique Car Features

| Feature          | FastCar | SlowCar | FancyCar |
| ---------------- | :-----: | :-----: | :------: |
| Max Speed        |   3x    |  .75x   |    2x    |
| Acceleration     |   2x    |  .75x   |    1x    |
| Brake Efficiency |   1x    |   2x    |    1x    |

### FancyCar

1. drive/reverse gear change
   - changes the direction of the car [`drive` or `reverse`]. Total distance is additive no matter the direction; relative distance to 'home' will change depending on direction
   - cars can only change gears if speed is 0
   - speed of a car going in reverse is still tracked as positive
2. horn
   - Has a horn that goes "beep beep"

---

# Instructions

### Necessary Requirements:
  1- Python **3.0** or Higher
  
  2- **PyTest** library for running test scripts
  

This project has been packaged and tested on both Windows and Linux platoforms. 
Simply clonning this repository should allow you to run the **main.py** file and the test scripts.

To run **main.py**, simply ``cd`` in this project's directory and then run the following command in your command prompt or terminal:

Linux:

``` 
python3 main.py 
```

Windows:

``` 
python main.py
```

After running this command the following is going to be printed on your terminal/command prompt (which is the solution to the problem statement):

```
--------------------------------------------------------------
                    FastCar's Dashboard                      
--------------------------------------------------------------
Engine = On
Headlights = On
Current Speed = 150 m/s
Odometer = 15600 m
Distance From Home = 15600 m
Current Gear = Drive
--------------------------------------------------------------
--------------------------------------------------------------
                    SlowCar's Dashboard                      
--------------------------------------------------------------
Engine = Off
Headlights = Off
Current Speed = 0 m/s
Odometer = 1125.0 m
Distance From Home = 1125.0 m
Current Gear = Park
--------------------------------------------------------------
--------------------------------------------------------------
                    FancyCar's Dashboard                      
--------------------------------------------------------------
Engine = On
Headlights = Off
Current Speed = 100 m/s
Odometer = 4665 m
Distance From Home = 1335 m
Current Gear = Reverse
--------------------------------------------------------------
beep beep
beep beep
```

---


In order to run the test scripts simply run the command ```pytest``` in your terminal while in this directory, and you should see a total of 74 tests pass. The following is going to be printed on your terminal:

```
tests/test_base_car.py ...............................................   [ 63%]
tests/test_fancy_car.py ...................                              [ 89%]
tests/test_fast_car.py ....                                              [ 94%]
tests/test_slow_car.py ....                                              [100%]

============================== 74 passed in 0.14s ==============================
```

In order to get a more detailed report of the tests run: ```pytest -v```

You can also run the test script for each file individually by running: ```pytest tests\script.py```

For example:
```
pytest -v tests/test_base_car.py
```

