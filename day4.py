from collections import defaultdict
from typing import DefaultDict
from baseFunctions import imp

pd = r'day4Inp.csv'

def returnDict(inList : list) -> dict:
   dic = defaultdict()
   for line in inList:
      lineSplit = line.replace('\n', '')
      lineSplit = lineSplit.split(' ')
      for entry in lineSplit:
         index = entry[:entry.find(':')]
         value = entry[entry.find(':') + 1:]
         dic[index] = value
   return dic

def checkHGT(hgt : str) -> bool:
   if hgt[-2:] == 'cm':
      return 193 >= int(hgt[:-2]) >= 150

   elif hgt[-2:] == 'in':
      return 76 >= int(hgt[:-2]) >= 59

   return False

def checkHCL(hcl : str) -> bool:
   try:
      assert hcl[0] == '#' and len(hcl) == 7
      int(hcl[1:], 16)
      return True
   except (ValueError, AssertionError):
      return False

def buildPassports(csv : str) -> list:
   data = open(csv, 'r')
   data = data.readlines()
   breaks = []
   for i, x in enumerate(data):
      if x == '\n':
         breaks.append(i)

   entrys = []
   for x in range(len(breaks)-1):
      entrys.append(returnDict(data[breaks[x] + 1 : breaks[x + 1]]))
   
   entrys.append(returnDict(data[:breaks[0]]))
   entrys.append(returnDict(data[breaks[-1]:]))

   return entrys

req = {'byr' : lambda x: 2002 >= int(x) >= 1920, 'iyr' : lambda x: 2020 >= int(x) >= 2010, 'eyr' : lambda x: 2030 >= int(x) >= 2020, 'hgt' : lambda x: checkHGT(x),
 'hcl' : lambda x: checkHCL(x), 'ecl' : lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 'pid' : lambda x: len(str(x)) == 9}

def partOne(passDict : list) -> int:
   total = 0
   for passport in passDict:
      correct = 0
      for detail in passport:
         if detail in req and detail != 'cid':
            correct += 1
      if correct > 6:
         total += 1
   return total

def partTwo(passDict : list) -> int:
   total = 0
   for passport in passDict:
      correct = 0
      for detail in passport:
         if detail in req and detail != 'cid':
            if req[detail](passport[detail]): 
               correct += 1
      if correct > 6:
         total += 1
   return total

print(partTwo(buildPassports(pd)))