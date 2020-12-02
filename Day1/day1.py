import csv 
from itertools import combinations
list = []
inc = 0
with open ('input.txt') as csv_file:
    csv = csv.reader(csv_file, delimiter='\n')
    for row in csv:
        for x in row:
            x = int(x)
            list.append(x)
#PT 1
for x in list:
    attempt = (2020 - x)
    if attempt in list:
        print (attempt, x)
        print (attempt*x)
    else:
        continue
#PT2
def subset_sum(l, target):
    if len(l) < 3:
        return False

    for ki, i in enumerate(l): #check List 1
        for kj, j in enumerate(l): #check list 2
            for kk, k in enumerate(l): #check list 3
                if kk != kj and kk != ki and kj != ki and i + j + k == target:
                #if list enums are not the same (aka not the same numbers) and they add up to target
                    print(i*j*k) 


subset_sum(list,2020)