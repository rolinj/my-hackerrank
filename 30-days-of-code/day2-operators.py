#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_amount = meal_cost * (tip_percent/100)
    tax_amount = meal_cost * (tax_percent/100)

    return round(meal_cost + tip_amount + tax_amount)
    

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))