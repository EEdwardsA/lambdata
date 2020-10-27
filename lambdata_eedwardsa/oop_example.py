"""OOP examples for module 2"""

import pandas as pd 
import numpy as np 


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for complex numbers
        Complex numbers have a real part and imaginary part.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class Animal:
    """General representation of animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return "vroom, vroom, I travel quickly"

    def eat(self, food):
        return "Huge fan of that " + str(food)


class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps):
        super().__init__(name, weight, diet_type)
        self.num_naps = int(num_naps)

    def say_something(self):
        return "This is sloths of typing"

    def run(self):
        return "I am too slow to run"

if __name__ == '__main__':
    num1 = Complex(3, 5)
    num2 = Complex(4, 2)
    num1.add(num2)
    print(num1.r, num1.i)

    user1 = SocialMediaUser('Justin', 'Provo')
    user2 = SocialMediaUser('Nick', 'Logan', 200)
    user3 = SocialMediaUser(name='Carl', location='Costa Rica', upvotes=1000)
    user4 = SocialMediaUser('George Washington', 'Delaware', 2)
    print("name: {}, is popular: {}. num upvotes: {}".format(
        user4.name, user4.is_popular(), user4.upvotes))
    print('name: {}, is popular: {}, num upvotes: {}'.format(
        user3.name, user3.is_popular(), user3.upvotes))
