from typing import Counter
from baseFunctions import imp

pwds = imp(r'day2inp.csv')

def partOne(inp : list) -> int:
   total = 0
   for password in inp:
      mn = int(password[:password.find('-')])
      mx = int(password[password.find('-') + 1: password.find(' ')])
      letter = password[password.find(' ') + 1]
      check = password[password.find(' ') + 4:]
      check = Counter(check) # counter returns a dictionary with the number of letter in the given str {letter : amount, letter : amount}
      if mx >= check[letter] >= mn:
         total += 1
   return total

def partTwo(inp : list) -> int:
   total = 0
   for password  in inp:
      first = int(password[:password.find('-')])
      second = int(password[password.find('-') + 1: password.find(' ')])
      letter = password[password.find(' ') + 1]
      check = password[password.find(' ') + 4:]
      if sum([check[first-1] == letter, check[second-1] == letter]) == 1:
         total += 1

   return total

print(partTwo(pwds))