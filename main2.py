import random
import math

'''
def isPrime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True
'''
def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    #print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True  

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

'''Main Program'''
e = 0
d = 0
t = 0
n = 0
while(True):
    #Variable
    restart = False

    #Select two prime number, p & q
    p = random.randint(50, 100)
    q = random.randint(50, 100)
    if(not (isPrime(p) and isPrime(q)) or p == q):
        continue

    #Calculate product
    n = p * q

    #Calculate totient
    t = (p - 1) * (q - 1)
    #print('t:', t)

    '''
    Public key:
    1. Prime number
    2. less than totient
    3. NOT a factor of totient
    '''
    while(True):
        e = random.randint(4, t-1)

        if(not isPrime(e)):
            continue

        #if(t % e != 1):
        if(getGCD(e, t) != 1):
            continue

        break

    #Private key
    #(D * E) MOD t == 1
    tested = [False] * t
    while(True):
        d = random.randint(2, t)

        #Check
        tested[d-2] = True
        for i in range(2, len(tested)):
            if(not tested[i]): 
                break
            
            restart = True
            break

        if(restart):
            break
        
        if((d*e) % t == 1):
            break
    if(restart):
        continue

    #End
    break
print('p:', p, type(p), ', q:', q, type(q))
print('n:', n, type(n))
print('t:', t, type(t))
print('E:', e, type(e))
print('D:', d, type(d))

data = 99

#Encryption, M^E MOD N
#encrypt_data = math.pow(data, e) % n
encrypt_data = (data ** e) % n
print('[Encrypt]', encrypt_data)

#Decryption, M^D MOD N
#decrypt_data = math.pow(encrypt_data, d) % n
decrypt_data = (encrypt_data ** d) % n
print('[Decrypt]', decrypt_data)

#Checking
if(decrypt_data == data):
    print("Success")
else:
    print("Failed")