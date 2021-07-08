def imp(filePath):
   nums=[]
   with open(filePath, 'r') as inp:
      for line in inp.readlines():
         try:
            nums.append(int(line.strip('\n')))
         except:
            nums.append(line.strip('\n'))
   return nums