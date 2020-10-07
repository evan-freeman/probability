"""
Let's do some roulette simulations!

We'll start with the American Wheel, which is worse for players.

House advantage is about 5%

I'll use -1 to denote 00, because 00 is not a number
"""

from numpy.random import randint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json


class Roulette:
    def __init__(self):
        self.wheel = {
            -1: {"color": "green"},
            0: {"color": "green"},
            1: {"color": "red"},
            2: {"color": "black"},
            3: {"color": "red"},
            4: {"color": "black"},
            5: {"color": "red"},
            6: {"color": "black"},
            7: {"color": "red"},
            8: {"color": "black"},
            9: {"color": "red"},
            10: {"color": "black"},
            11: {"color": "black"},
            12: {"color": "red"},
            13: {"color": "black"},
            14: {"color": "red"},
            15: {"color": "black"},
            16: {"color": "red"},
            17: {"color": "black"},
            18: {"color": "red"},
            19: {"color": "red"},
            20: {"color": "black"},
            21: {"color": "red"},
            22: {"color": "black"},
            23: {"color": "red"},
            24: {"color": "black"},
            25: {"color": "red"},
            26: {"color": "black"},
            27: {"color": "red"},
            28: {"color": "black"},
            29: {"color": "black"},
            30: {"color": "red"},
            31: {"color": "black"},
            32: {"color": "red"},
            33: {"color": "black"},
            34: {"color": "red"},
            35: {"color": "black"},
            36: {"color": "red"},
        }

        self.payout = {"straight": 35, "color": 1, "parity": 1}

        self.results = []

        for num in self.wheel:
            if num <= 0:
                self.wheel[num]["parity"] = "none"
            elif num % 2 == 0:
                self.wheel[num]["parity"] = "even"
            elif num % 2 == 1:
                self.wheel[num]["parity"] = "odd"

    @staticmethod
    def roll():
        return randint(-1, 37)

    def bet(self, type, choice):
        result = self.roll()
        win = False
        if type == "straight":
            if choice == result:
                win = True
        if type in ["color", "parity"]:
            if choice == self.wheel[result][type]:
                win = True
        else:
            print(
                "I don't understand that bet. Please choose one of the following bets: \nstraight\ncolor\nparity"
            )
            return False
        return (result,)

