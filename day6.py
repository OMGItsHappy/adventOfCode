from collections import defaultdict


def returnSet(inList : list) -> list:
   temp = []
   for x in inList:
      temp.append(set(x.replace('\n', '')))
   return temp

def buildPassports(csv : str) -> list:
   data = open(csv, 'r')
   data = data.readlines()
   breaks = []
   for i, x in enumerate(data):
      if x == '\n':
         breaks.append(i)

   entrys = []
   for x in range(len(breaks)-1):
      entrys.append(returnSet(data[breaks[x] + 1 : breaks[x + 1]]))
   
   entrys.append(returnSet(data[:breaks[0]]))
   entrys.append(returnSet(data[breaks[-1] + 1:]))

   return entrys

answers = buildPassports('day6Inp.csv')

def partOne(answers : list) -> int:
   total = 0
   for x in answers:
      tempSet = set()
      for y in x:
         tempSet.update(y)
      total += len(tempSet)
   return total

def partTwo(answers : list) -> int:
   total = 0
   for x in answers:
      tempDic = defaultdict()
      for y in x:
         for z in y:
            try:
               tempDic[z] += 1
            except KeyError:
               tempDic[z] = 1

      for y in tempDic:
         if tempDic[y] == len(x):
            total += 1
   return total
