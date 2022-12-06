from colorama import Fore
from utility import Powerball


class PrizeSelector(Powerball):

    def results(self):
        """" under of this class i created prizeselector that is show the result that the user numbers compare
         with the winning number and if the user is lucky and got White balls and powerball number will won the prize"""

        intersect = len(set(self.luckyNumber).intersection(set(self.winningNumber)))
        commonNumbers = (set(self.winningNumber)).intersection(set(self.luckyNumber))
        print(Fore.LIGHTWHITE_EX + f"Correct white balls: {intersect} )")
        print("The common Numbers are:", commonNumbers)
        if intersect == 5 and self.luckyNumber == self.winningNumber:
            print("Bingo You won☺♥☺♥!! you have 5 correct white balls and the power ball \nYou won Jackpot 324,000,000$")
        elif intersect == 5 and self.luckyNumber != self.winningNumber:
            print("Congratulations☺☺!! you have 5 correct white balls without the power ball \nYou won 1,000,000$")
        elif intersect == 4 and self.luckyNumber == self.winningNumber:
            print("Congra♥!! you have 4 correct white balls and the power ball \nYou won: 10,000 $")
        elif intersect == 4 and self.luckyNumber != self.winningNumber:
            print("Congra♥!! you have 4 correct white balls and no power ball \nYou won: 100$")
        elif intersect == 3 and self.luckyNumber == self.winningNumber:
            print("Congra♥!! you have 3 correct white balls and  power ball \nYou won: 100$")
        elif intersect == 3 and self.luckyNumber != self.winningNumber:
            print("Congra♥!! you have 3 correct white balls and  no power ball \nYou won: 7$")
        elif intersect == 2 and self.luckyNumber == self.winningNumber:
            print("Congra♥!! you have 2 correct white balls and power ball \nYou won: 7$")
        elif intersect == 1 and self.luckyNumber == self.winningNumber:
            print("congra ♥!! you have 1 correct white balls and power ball \nYou won: 4$")
        elif intersect == 0 and self.luckyNumber == self.winningNumber:
            print("Congra!! you have just power ball \n You win: 4$")
        else:
            print("Sorry You lose it, try again please!")






