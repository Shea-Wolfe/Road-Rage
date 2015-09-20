import numpy as np
import random
import statistics as st
import matplotlib.pyplot as plt
import math


class Car():

    def __init__(self, location, current_speed=25, limit=33):
        self.max_s = limit #In meters per second truncating 33.333 to 33
        self.length = 5 #In meters
        self.cs = current_speed #current speed
        self.location = location
        self.distance = 0



    def change_speed(self):
        choice = random.random()
        if self.location >= 1000 and self.location < 2000:
            if choice < .14:
                self.cs -= 2
            elif self.cs == self.max_s:
                pass
            else:
                self.cs += 2
                if self.cs > self.max_s:
                    self.cs = self.max_s
        elif self.location >= 3000 and self.location < 4000:
            if choice < .2:
                self.cs -= 2
            elif self.cs == self.max_s:
                pass
            else:
                self.cs += 2
                if self.cs > self.max_s:
                    self.cs = self.max_s
        elif self.location >= 5000 and self.location < 6000:
            if choice < .12:
                self.cs -= 2
            elif self.cs == self.max_s:
                pass
            else:
                self.cs += 2
                if self.cs > self.max_s:
                    self.cs = self.max_s
        else:
            if choice < .1:
                self.cs -= 2
            elif self.cs == self.max_s:
                pass
            else:
                self.cs += 2
                if self.cs > self.max_s:
                    self.cs = self.max_s


    def drive(self):
        self.location += self.cs
class Road():

    def __init__(self):
        pass

    def pop_road(self, limit):
        self.cars = [Car(int((n*33.33)+4), limit=limit) for n in range(30)]


    def get_car_locations(self, car):
        return self.cars[car]

    def check_speed(self, car):
        if car == 29:
            pass
        elif (self.cars[car].location + self.cars[car].cs) >= (self.cars[car+1].location - 4):
            self.cars[car].cs = self.cars[car+1].cs

    def crash(self, car):
        if car == 29:
            pass
        elif (self.cars[car].location + self.cars[car].cs) >= (self.cars[car+1].cs + self.cars[car+1].location - 4):
            self.cars[car].location = self.cars[car+1].cs + self.cars[car+1].location - 5
            self.cars[car].cs = 0
        else:
            pass

class Simulation():

    def __init__(self, limit):
        self.road = Road()
        self.road.pop_road(limit)
        self.crash = 0
        self.car_speed = []
        self.car_locations = [1] * 1000
        self.all_locations = []

    def add_location(self, car):
        self.car_locations[self.road.cars[car].location] = 0
        self.car_locations[(self.road.cars[car].location) - 1] = 0
        self.car_locations[(self.road.cars[car].location) - 2] = 0
        self.car_locations[(self.road.cars[car].location) - 3] = 0
        self.car_locations[(self.road.cars[car].location) - 4] = 0

    def tick(self):
        for car in range(30):
            self.road.cars[car].change_speed()   #Car decides to speed up or slow down.
            self.road.check_speed(car) #Car checks if there's a car in its "zone of danger"
        for car in range(30):
            self.road.crash(car) #Checks for crashes now that we've set the data
            if self.road.cars[car].cs == 0:
                self.crash += 1
            self.road.cars[car].drive() #actually makes dem boats go
            self.car_speed.append(self.road.cars[car].cs)
            if  self.road.cars[car].location >= 1000:
                self.road.cars.insert(0,Car(((30-car) * 5) - 1,self.road.cars[car].cs))
                del self.road.cars[car + 1] #Gets rid of cars that drive off the end
                self.add_location(0)
            else:
                self.add_location(car)

        self.final_speeds = self.car_speed
        self.all_locations.append(self.car_locations)
        self.car_speed = []
        self.car_locations = [1] * 1000
