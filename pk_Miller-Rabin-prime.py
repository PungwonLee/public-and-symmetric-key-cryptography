import random
def mod_exp(a,e,n):
    binary=format(e,'b')
    res=1
    for i in binary:
        res=res**2
        if i=='1': res*=a
        res=res%n
    return res  

def exp(a,e):
    binary=format(e,'b')
    res=1
    for i in binary:
        res=res**2
        if i=='1': res*=a
        res=res
    return res  

def miller_rabin_test(n,b,s,t):
    
    if  (mod_exp(b,t,n) == (1 % n)): return 1
    if  (mod_exp(b,t,n) == (-1 % n)): return 1
    for i in range(1,s):
        if mod_exp(b,t*(2**i),n) == (1 % n):
            return 0
        if mod_exp(b,t*(2**i),n) == (-1 % n):
            return 1
        
    return 0    

def is_prime (n):
    
    n_1=n-1
    
    s=0
    i=2
    while n_1:
        if(n_1%i==0):
            n_1=n_1//i
            s=s+1
        else:
            t=int(n_1)
            
            break
    for i in range(20):
        b = random.randint(2,n-1)
          
        if miller_rabin_test(n,b,s,t)==1:
            return 1
    return 0           


print("is_prime(561)=",is_prime(561))
print("is_prime(569)=",is_prime(569))
print("is_prime(2 ** (2 ** 4) + 1)=",is_prime(2 ** (2 ** 4) + 1))
print("is_prime(2 ** (2 ** 10) + 1)=",is_prime(2 ** (2 ** 10) + 1))
print("is_prime(2 ** 1279-1)=",is_prime(2 ** 1279-1))
print("is_prime(2 ** 2203-1)=",is_prime(2 ** 2203-1))
print("is_prime(2 ** 3217-1)=",is_prime(2 ** 3217-1))
