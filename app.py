from utility import Powerball
from colorama import Fore
from prizes import PrizeSelector


def app():
    pri = PrizeSelector()

    pri.create_number()
    pri.show()
    pri.results()




