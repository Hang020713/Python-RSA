#Get input
data = []
num = 0
while not(num == -1):
    num = int(input('number(-1 out):'))
    if(not(num == -1)):
        data.append(num)

#Find all factors for all numbers
factors = []
min_factor_index = 0
now_num = 0
for n in data:
    factors.append([])
    for f in range(1, n+1):
        if(n % f == 0):
            factors[now_num].append(f)

    #Find min length
    if(len(factors[now_num]) < len(factors[min_factor_index])):
        min_factor_index = now_num

    now_num += 1
print("Original: ", factors)

#Reduce factors set datas with min length
for f in range(len(factors)):
    for i in range(len(factors[f])):
        if(factors[f][i] > factors[min_factor_index][-1]):
            factors[f] = factors[f][:i]
            break
print("Cut: ", factors)

#Find same
common_factor = -1
for i in reversed(factors[0]):
    same = False

    for f in factors[1:]:
        for n in reversed(f):
           #Check same
           if(i == n):
               same = True
               break 
        
        #All number same
        if(same):
            break
    
    #Common factor
    if(same):
        common_factor = i
        break

#Print common factor
if(common_factor == -1):
    print("there is no common factor for them")
else:
    print("common factor:", common_factor)