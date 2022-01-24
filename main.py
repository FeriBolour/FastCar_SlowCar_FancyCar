"""
Main Function for Problem Statement

@author: Farshad Bolouri
"""

from fancy_car import FancyCar
from fast_car import FastCar
from slow_car import SlowCar

def main():
    fastC = FastCar()
    slowC = SlowCar()
    fancyC = FancyCar()
    # 1. All three cars start their engines
    fastC.on()
    slowC.on()
    fancyC.on()
    # 2. FastCar and FancyCar turn on their lights
    fastC.headlights = True
    fancyC.headlights = True
    # 3. All three cars gas for 11 seconds
    fastC.gas(11)
    slowC.gas(11)
    fancyC.gas(11)
    # 4. All three cars drive for 30 seconds
    fastC.drive(30)
    slowC.drive(30)
    fancyC.drive(30)
    # 5. FancyCar brakes for 5 seconds, slowing down in order to enjoy the 
    #    scenery around it, then continues driving for 3 seconds
    fancyC.brake(5)
    fancyC.drive(3)
    # 6. SlowCar brakes for 6 seconds, curious what FancyCar is looking at
    slowC.brake(6)
    # 7. FancyCar realizes they left their lucky keychain behind and 
    #    immediately brakes to a full stop, changes to reverse, gases for 20 
    #    seconds, then drives for an additional 30 seconds
    fancyC.brake("Stop") # Using "break to a fullstop" option
    fancyC.gear = "Reverse"
    fancyC.gas(20)
    fancyC.drive(30)
    # 8. After realizing headlights aren't that useful while going in reverse, 
    #    FancyCar turns off its lights
    fancyC.headlights = False
    # 9. FastCar , all the while, continues driving for another 30 seconds, 
    #    gasses 20 seconds, and drives an addition 60 seconds
    fastC.drive(30)
    fastC.gas(20)
    fastC.drive(60)
    # 10. SlowCar feels lonely (now that both cars have left it behind), comes
    #     to a full stop, then turns off its engine
    slowC.brake("Stop")
    slowC.off()
    # 11. All three cars check their dashboards
    fastC.stats()
    slowC.stats()
    fancyC.stats()  
    # 12. FancyCar honks its horn twice, celebrating that it found its lost
    #     keychain
    fancyC.horn()
    fancyC.horn()
    
    
if __name__ == '__main__':
    main()