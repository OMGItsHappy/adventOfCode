from baseFunctions import imp

passes = imp(r'day5Inp.csv')

def FB(bottom : int, top : int, direction : str):
   if top - 1 == bottom:
      if direction in ['F', 'L']:
         return bottom 
      elif direction in ['B', 'R']:
         return top
   elif direction in ['F', 'L']: #lower half
      temp = top - bottom
      temp /= 2
      top = int(temp) + bottom
   elif direction in ['B', 'R']: # upper half
      temp = top - bottom
      temp = temp/2
      bottom += int(temp) + 1
   return bottom, top

def partOne(passes):
   ids = []
   for test in passes:
      bottom, top = 0, 127
      for x in test[:6]:
         bottom, top = FB(bottom, top, x)

      row = FB(bottom, top, test[6])

      bottom, top = 0, 7
      for x in test[7:-1]:
         bottom, top = FB(bottom, top, x)

      column = FB(bottom, top, test[-1])

      seatID = row * 8 + column
      ids.append(seatID)
   return ids

def partTwo(ids):
   ids = sorted(ids)
   start = ids[1]
   for i, x in enumerate(ids[1:-1]):
      if x != start:
         return start
      start += 1

print(partTwo(partOne(passes)))