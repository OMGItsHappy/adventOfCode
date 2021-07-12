from collections import defaultdict
from baseFunctions import imp
import json

bags = imp(r'day7Inp.csv')

contained = defaultdict()

for x in bags:

   temp = defaultdict()

   contain = x.split('bag')
   contain = [line[:-1] for line in contain]
   
   outerBag = contain[0]
   temp.update({outerBag : defaultdict()})
   contain = contain[1:-1]   

   if 's contain no other' != contain[0]:
      for y in contain:
         tempList = y.split(' ')
         bag = tempList[-2] + ' ' + tempList[-1]
         num = int(tempList[-3])
         temp[outerBag].update({bag : num})

   contained.update(temp)

#print(json.dumps(contained, indent = 1))

def containsShiny(inBag : str) -> bool:
   global contained

   if 'shiny gold' in contained[inBag]:
      return True

   for x in contained[inBag]: 
      if containsShiny(x) == True:
         return True

   return False


def partOne(inDict : dict) -> int:
   total = 0
   for x in inDict:
      if containsShiny(x):
         print(x, 'contains gold')
         total+= 1
   return total

def partTwo(inDict : dict) -> int:
   start = inDict['shiny gold']
   buildDict = start
