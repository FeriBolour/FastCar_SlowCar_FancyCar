"""
Base Car Class

@author: Farshad Bolouri
"""

class BaseCar:
    
    # Private Member
    __switchDisp = ['Off', 'On']
    
    # Protected Attributes
    _gearModes = ["Park", "Drive"]

    # Average Car Stats -- Protected Members
    _maxSpeed = 50
    _acceleration = 5
    _brakeEfficiency = -10
    
    # Dashboard Info -- Protected Members
    _speed = 0
    _odometer = 0
    _home = 0
    _gear = _gearModes[0]
    
    # constructor
    def __init__(self, engine = False, headlights = False):
        try:
            assert isinstance(engine, bool) and isinstance(headlights, bool)  \
                , "Invalid input for either Engine or Headlights!\n" \
                    "Only accepting Boolean values."
            # Protected Members
            self._engine = engine
            self._headlights = headlights
        except AssertionError as msg:
            print(msg)
    
    # Neccessary Getter and Setter methods for the Protected Members
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, switch):
        try:
            assert isinstance(switch, bool), "Invalid input for Engine!\n" \
                "Only accepting Boolean values."
            self._engine = switch
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------
    @property 
    def headlights(self):
        return self._headlights
    
    @headlights.setter
    def headlights(self, switch):
        try:
            assert isinstance(switch, bool), "Invalid input for headlights!\n" \
                "Only accepting Boolean values."
            self._headlights = switch
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------
    @property 
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speedValue):
        try:
            float(speedValue)
            self._speed = speedValue
            
        except ValueError:
            print("Invalid input for speed!\nOnly accepting Float or Integer values.")
    #--------------------------------------------------------------------------
    @property 
    def odometer(self):
        return self._odometer
    
    @odometer.setter
    def odometer(self, odometerValue):
        try:
            float(odometerValue)
            self._odometer = odometerValue
        except ValueError:
            print("Invalid input for odometer!\nOnly accepting Float or Integer values.")
    #--------------------------------------------------------------------------
    @property 
    def home(self):
        return abs(self._home)
    
    @home.setter
    def home(self, homeDistance):
        try:
            float(homeDistance)
            self._home = homeDistance
        except ValueError:
            print("Invalid input for Distance From Home!\nOnly accepting Float or Integer values.")
    #--------------------------------------------------------------------------
    @property
    def gear(self):
        return self._gear
    
    @gear.setter
    def gear(self, mode):
        try:
            assert isinstance(mode, str), "Invalid input for Gear!\n" \
                "Only accepting String values."
            mode = mode.capitalize()

            if self._gear != mode:
                if self.speed == 0 or self._gear == 'Park':
                    if mode in self._gearModes:
                        self._gear = mode
                    else:
                        print("This gear does not exist!")
                        print("--------------------------------------------------------------")
                        
                else:
                    print("Can't change gears while still moving!")
                    print(f"Current Speed = {self.speed} m/s")
                    print("--------------------------------------------------------------")
                
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # Turn Off Engine
    def off(self):
        if self.speed == 0:
            self.engine = False
        else:
            print("Can't turn off Engine while still moving!")
            print(f"Current Speed = {self.speed}")
            print("--------------------------------------------------------------")
    #--------------------------------------------------------------------------
    # Turn On Engine
    def on(self):
        self.engine = True
        self.home = 0    # Establishing Starting Point
    #--------------------------------------------------------------------------
    # Accelrating the car
    def gas(self, gasTime):
        try:
            float(gasTime)
            
            if self.engine == True:
                self.speed = self._acceleration * gasTime + self.speed         # v = a*t + v0
                if self.speed > self._maxSpeed:
                    self.speed = self._maxSpeed
                    
            else:
                print("Can't accelerate while the engine is turned off!")
                print("--------------------------------------------------------------")
                
        except ValueError:
            print("Invalid input for Gas Time!\nOnly accepting Float or Integer values.")
    #--------------------------------------------------------------------------   
    # Continue driving in the same direction for a specific amount of time
    def drive(self, driveTime):
        try:
            float(driveTime)
            
            if self.engine == True:       
                if self.gear == 'Park':
                    self.gear = 'Drive'
                self.home = self.home + self.speed * driveTime                 # x = x0 + v*t
                self.odometer = self.odometer + self.speed * driveTime         # x = x0 + v*t
                
            else:
                print("Can't drive while the engine is turned off!")
                print("--------------------------------------------------------------")
                
        except ValueError:
            print("Invalid input for Drive Time!\nOnly accepting Float or Integer values.")
    #--------------------------------------------------------------------------   
    # Slowing down the Vehicle
    def brake(self, brakeTime):
        try:
            assert isinstance(brakeTime, str) or isinstance(brakeTime, float) \
                or isinstance(brakeTime, int), "Invalid input for Brake\n" \
                    "Only accepting String, Float, or Integer values."
                    
            if isinstance(brakeTime, str):
                brakeTime = brakeTime.capitalize()  # In case the user didn't captilize the Stop!
                
            if not isinstance(brakeTime, str):  
                if self.engine == True:
                    self.speed = self._brakeEfficiency * brakeTime + self.speed# v = a*t + v0
                    
                    if self.speed < 0:  # if the car comes to full stop  
                        self.speed = 0
                        self.gear = "Park"      
                        
                else:
                    print("Can't brake while the engine is turned off!")
                    print("--------------------------------------------------------------")
                    
            elif brakeTime == "Stop":   #Fullstop Option
                self.speed = 0
                self.gear = "Park"
                
            else:
                print("Invalid input for Brake")
                
        except AssertionError as msg:
            print(msg)
    #--------------------------------------------------------------------------    
    # Check Dashboard
    def stats(self):
        print("--------------------------------------------------------------")
        print(f"Engine = {self.__switchDisp[self.engine]}")
        print(f"Headlights = {self.__switchDisp[self.headlights]}")
        print(f"Current Speed = {self.speed} m/s")
        print(f"Odometer = {self.odometer} m")
        print(f"Distance From Home = {self.home} m")
        print(f"Current Gear = {self.gear}")
        print("--------------------------------------------------------------")
