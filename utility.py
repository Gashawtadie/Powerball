import random

from colorama import Fore
from random import randint


class Powerball:
    """ under this class i create the Attributor that is bring(Append numbers from generator)
    numbers form create number methods and crete random numbers for both today lottery nuber and users lucky number"""

    def __init__(self):
        self.winningNumber = []
        self.powerballToday = []
        self.luckyNumber = []
        self.powerballlucky = []

    def create_number(self):
        """ this method is under power class and function is create the numbers for both winning number
        and lucky number"""
        for i in range(1, 6):
            """ this for loop create the daily winning numbers only 5 ranges and up to 1-20 numbers"""
            self.winningNumber.append(randint(1, 20))
            self.winningNumber.sort()
            self.powerballToday = random.randint(1, 10)

            self.luckyNumber.append(randint(1, 20))
            self.luckyNumber.sort()
            self.powerballlucky = random.randint(1, 10)


    def show(self):

        """ in this method i use the variable that is Append from the "self,wiinning number" like string
        but by using the "winNumbur += str(f" {variable} "
        by spliting each numbers its possible to split the numbers  """
        print(Fore.BLUE, f" ♦♦♦ Welcome to MIFAL HAPAIS ♦♦♦")
        winNumbers = " "
        for num in self.winningNumber:
            winNumbers += str(f" {num} ")
        print(Fore.LIGHTWHITE_EX + "Today’s Powerball winning numbers:\n", Fore.MAGENTA + winNumbers,
              Fore.YELLOW + str(self.powerballToday))

        lucNumber = " "
        for num in self.luckyNumber:
            lucNumber += f" {num} "
        print(Fore.LIGHTWHITE_EX + "Your lucky numbers is:\n", Fore.MAGENTA + lucNumber,
              Fore.YELLOW + str(self.powerballlucky))
        print()
    # def intersection(self):
    #     intersect = len(set(self.winningNumber).intersection(set(self.luckyNumber)))
    #     print(Fore.LIGHTWHITE_EX + f"Correct white balls: {intersect}")

# gashu = Powerball()
# gashu.create_number()
# gashu.show()
# gashu.intersection()

