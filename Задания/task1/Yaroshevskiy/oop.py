from time import time, sleep
from random import random


class Car:
    def __init__(self, model: str = "Aston Martin",
                 color: str = "Black",
                 volume: int = 30,
                 consp: int = 1):
        self.model = model
        self.color = color
        self.all_volume = volume
        self.volume = volume
        self.consumption = consp

    def start(self) -> int:
        self.start_time = int(time())
        return self.volume // self.consumption

    def stop(self) -> int:
        self.volume -= self.consumption * (int(time()) - self.start_time)
        return self.volume

    def show_info(self) -> None:
        print(
            f"model: {self.model}; color: {self.color}; all volume: {self.all_volume}; volume left: {self.volume}")


car = Car(volume=10)

time_sleep = int(car.start() * random())
print(f"time for working: {time_sleep} seconds")

sleep(time_sleep)

car.stop()
car.show_info()
