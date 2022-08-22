'''RaceCar


Now we need a RaceCar in our cars world

You are given two  classes Car and RaceCar

A Race Car is a Car but with the additional behaviours'

Inherit the Car class into RaceCar Class and build the additional features

implement the car and RaceCar classes with described attributes and methods


RaceCar have following attributes and methods
Attributes:
color,max_speed,acceeleration,tyre_friction,is_engine_started,current_speed,nitro
note: nitro is race_car attributes as child attribute

Methods:
start_engine,stop_engine,accelerate,apply_breaks,sound_horn

override Methods:
1. sound_horn:
   print peeppeep or beep beep if Race_car engine is on 
   print car has not started yet if Race_car engine is off

2.accelerate:
    when car accelerates when nitro points are available the current_spped will be add 20 within max limits and nitro get reduced by 1 point 



racecar = color:"red",max_speed=250,acceleration =50,tyre_friction=30,nitro=4'''


class Car(object):
    def __init__(self,color,max_speed,acceeleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceeleration=acceeleration
        self.tyre_friction=tyre_friction
        


    def start_engine(self):
        print("The Engine is Started")
        

    def stop_engine(self):
        print("The Engine is not started yet.")
    def accelerate(self):
        pass
    def apply_breaks(self):
        pass
    def sound_horn(self):
        
        pass


class Race_car(Car):
    def __init__(self,color,max_speed,acceeleration,tyre_friction,nitro):
        self.nitro=nitro

        
        
    
    
    
