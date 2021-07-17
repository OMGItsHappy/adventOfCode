from baseFunctions import imp

data = imp(r'day2Inp.csv')
total = 0
for x in data:
   if sum([x[x.find(':') + 2:][int(x[x.find('-') + 1 : x.find(' ')]) - 1] == x[x.find(':') - 1], x[x.find(':') + 2:][int(x[:x.find('-')]) - 1] == x[x.find(':') - 1]]) == 1: total += 1

print(total)
