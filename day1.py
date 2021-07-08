from baseFunctions import imp

nums = imp(r'day1Inp.csv')

def partOne(inNums : list) -> int:
    for x in inNums:
        for y in inNums:
            if x + y == 2020:
                return x*y

def partTwo(inNums : list) -> int:
    for x in nums:
        for y in nums:
            for z in nums:
                if x + y + z == 2020:
                    return x*y*z

