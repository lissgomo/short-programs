'''
Draws a random card from the deck and displays card,
'''

import random
import itertools

v = [str(x) for x in range(2, 11)] + list("JQKA")
s = [str(x) for x in list("♠♣♥♦")]


class Card:
    def __init__(self,value=v,suit=s):
        self.value = value
        self.suit = suit
        
        value = random.shuffle(v)
        suit = random.shuffle(s)   
        
    def print(self):
        digits = self.value[0]
        
        if digits == '10': 
            print('┌───────┐')
            print(f'| {self.value[0]}    |')
            print('|       |')
            print(f'|   {self.suit[0]}   |')
            print('|       |')
            print(f'|     {self.value[0]}|')
            print('└───────┘')
        else: #else is not working
            print('┌───────┐')
            print(f'| {self.value[0]}     |')
            print('|       |')
            print(f'|   {self.suit[0]}   |')
            print('|       |')
            print(f'|     {self.value[0]} |')
            print('└───────┘') 
            
if __name__ == '__main__':
    x=Card()
    x.print()
