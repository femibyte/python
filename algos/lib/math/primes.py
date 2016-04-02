import math
def isPrime(n):
    if n <= 1 or n%2==0: return False 
    if n==2: return True
    ulim = int(math.sqrt(n))+1
    for i in range(3,ulim+1,2):
        if n%i ==0:
            return False
    return True


  def sieveErastothenes(n):
    primesBool = [True]*(n+1)   # Initialize array of size n+1 due to zeroth indexing
    primesBool[0] = False
    primesBool[1] = False
    uLim = int(math.sqrt(n))+1  # Upper limit due to range in Python only using int args
    for i in range(2, uLim):
        if primesBool[i]==True: # Not yet processed hence is prime
            k = i*i  # Start from i*i since i*j for any j<i will have already been processed
            while (k<=n):
                primesBool[k]=False
                k+=i #Increment by i onwards to get i*(i+1) etc
    primes = [j for j in range(0, len(primesBool)) if primesBool[j]]
    return primes
    