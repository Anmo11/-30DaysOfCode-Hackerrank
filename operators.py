import math
import os
import random
import re
import sys

mealcost = float(input())
tippercent=int(input())
taxpercent=int(input())
def totalcost(): 
    tipcost= (tippercent*(1/100))*mealcost
    taxcost= (taxpercent*(1/100))*mealcost
    totalcost= mealcost + tipcost + taxcost
    print(round(totalcost))    
totalcost()
