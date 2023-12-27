import random
import math

def isPrime(num):
    prime = False
    for i in range(2,num):
        if (num % i) == 0:
            prime = False
        else:
            prime = True
    return prime

def getGCD(num1, num2):
    #Get input
    data = [num1, num2]

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
    #print("Original: ", factors)

    #Reduce factors set datas with min length
    for f in range(len(factors)):
        for i in range(len(factors[f])):
            if(factors[f][i] > factors[min_factor_index][-1]):
                factors[f] = factors[f][:i]
                break
    #print("Cut: ", factors)

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
    return common_factor

def getLCM(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

n = 0
d = 0
e = 0
while True:
    #Generate random prime number q & d
    p = 1
    q = 1

    while not (isPrime(p) and isPrime(q)):
        p = random.randint(300, 500)
        q = random.randint(300, 500)
    print("p", p, ", q", q)
    n = p * q
    print("n:", n)

    #Find L, lcm(p-1, q-1)
    #l = getLCM(p-1, q-1)
    l = math.lcm(p-1, q-1)
    print("l:", l)

    #Get E
    flag = True
    #for e in reversed(range(2, l-1)):
    for e in reversed(range(2, l-1)):
        if(math.gcd(e, l) == 1):
            flag = False
            break
    #No Same GCD as 1
    if(flag):
        print("e wrong")
        continue
    print("E:", e)

    #Get D
    flag = True
    #for d in reversed(range(2, l-1)):
    for d in reversed(range(2, l-1)):
        if((e * d) % l == 1):
            flag = False
            break
    if(flag):
        print("e wrong")
        continue
    print("D:", d)

    break

    #Checking
    original_str = "abc"
    entropy = 0
    for letter in original_str:
        entropy = entropy + ord(letter)

    encrypt = pow(entropy, e)
    encrypt %= n

    decrypt = pow(encrypt, d)
    decrypt %= n
    if(not decrypt == entropy):
        continue

    #End
    break

#Encrypt
original_str = "abc"
entropy = 0
for letter in original_str:
    entropy = entropy + ord(letter)
if(entropy > n):
    print("str too large")
    exit()

print("original:", entropy)

encrypt = pow(entropy, e)
encrypt %= n
print("encrypt:", encrypt)

decrypt = pow(encrypt, d)
decrypt %= n
print("decrypt:", decrypt)