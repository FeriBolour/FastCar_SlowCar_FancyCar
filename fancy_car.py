"""
Fancy Car Class

@author: Farshad Bolouri
"""

from base_car import BaseCar


class FancyCar(BaseCar):
    
    # Private Attributes
    __horn = "beep beep"
    
    # constructor
    def __init__(self, engine = False, headlights = False):
        try:
            assert isinstance(engine, bool) and isinstance(headlights, bool)  \
                , "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values."
            super().__init__(engine, headlights)
            #Fast Car Features
            self._maxSpeed = 2 * self._maxSpeed
            self._gearModes.append('Reverse')
            self.__prevDirection = 'Drive'
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------
    def horn(self):
        print(self.__horn)
    #--------------------------------------------------------------------------    
    # Overriding GEAR's setter method in base_car class
    @BaseCar.gear.setter
    def gear(self, mode):
        try:
            assert isinstance(mode, str), "Invalid input for Gear!\n" \
                "Only accepting String values."
            mode = mode.capitalize()   # In case the user didn't captilize the Gear

            if self._gear != mode:    
                if self.speed == 0 or self._gear == 'Park':
                    if mode in self._gearModes:               
                        if self._gear != 'Park':
                            self.__prevDirection = self._gear                   
                        self._gear = mode
                        
                    else:
                        print("This gear does not exist!")
                        print("--------------------------------------------------------------")
                        
                else:
                    print("Can't change gears while still moving!")
                    print(f"Current Speed = {self.speed}")
                    print("--------------------------------------------------------------")
                
        except AssertionError as msg:
            print(msg)

    #--------------------------------------------------------------------------
    # overriding the DRIVE function in base_car class to accomadate for reverse
    def drive(self, driveTime):
        try:
            float(driveTime)
            
            if self.engine == True:
                if self.gear == 'Park':
                    self.gear = self.__prevDirection
                    
                if self.gear == 'Drive':
                    self.home = self.home + self.speed * driveTime             # x = x0 + v*t
                elif self.gear == 'Reverse':
                    self.home = self.home - self.speed * driveTime
    
                self.odometer = self.odometer + self.speed * driveTime         # x = x0 + v*t
    
            else:
                print("Can't drive while the engine is turned off!")
                print("--------------------------------------------------------------")
                
        except ValueError:
            print("Invalid input for Drive Time!\nOnly accepting Float or Integer values.")
    #--------------------------------------------------------------------------   
    # overriding the BRAKE function in base_car class to accomadate for reverse
    def brake(self, brakeTime):
        try:
            assert isinstance(brakeTime, str) or isinstance(brakeTime, float) \
                or isinstance(brakeTime, int), "Invalid input for Brake\n" \
                    "Only accepting String, Float, or Integer values."
                    
            if isinstance(brakeTime, str):
                brakeTime = brakeTime.capitalize()  # In case the user didn't captilize the Stop!
                
            if not isinstance(brakeTime, str):
                if self.engine == True:
                    self.speed = self._brakeEfficiency * brakeTime + self.speed        # v = a*t + v0
                    
                    if self.speed < 0:  # if the car comes to full stop  
                        self.speed = 0
                        self.__prevDirection = self._gear
                        self.gear = "Park"
                
                else:
                    print("Can't brake while the engine is turned off!")
                    print("--------------------------------------------------------------")
                    
            elif brakeTime == "Stop":   #Fullstop Option
                self.speed = 0
                self.__prevDirection = self._gear
                self.gear = "Park"
                
            else:
                print("Invalid input for Brake")
                
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------                
    # Overriding the stats function from base class
    def stats(self):
        print("--------------------------------------------------------------")
        print("                    FancyCar's Dashboard                      ")
        super().stats()