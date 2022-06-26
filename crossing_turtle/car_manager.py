from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 300
STARTING_Y = [y for y in range(-250, 270, 20)]
NUMBER_OF_CARS = 20


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(STARTING_X, random.choice(STARTING_Y))
            car.setheading(180)
            self.car_list.append(car)

    def accelerate_cars(self):
        self.car_speed += MOVE_INCREMENT
