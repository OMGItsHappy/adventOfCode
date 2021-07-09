from baseFunctions import imp

hill = imp(r'day3Inp.csv')

def partOne(inp : list) -> int:
   total = 0
   toSide = 0
   vertical = 0
   down, right = 1, 3
   while vertical < len(inp) - 1:
      toSide += right
      vertical += down
      if inp[vertical][toSide%len(inp[vertical])] == '#':
         total += 1

   return total

def partTwo(inp : list) -> int:
   endTotal = 1
   for slope in [[1,1], [1,3], [1,5], [1,7], [2,1]]:
      toSide = 0
      total = 0
      toSide = 0
      vertical = 0
      down, right = slope[0], slope[1]
      while vertical < len(inp) - 1:
         toSide += right
         vertical += down
         if inp[vertical][toSide%len(inp[vertical])] == '#':
            total += 1
      endTotal *= total

   return endTotal
