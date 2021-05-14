def extended_gcd(a,b):
    if b==0:
        st=[[1,0],[0,1]]
        for i in range(len(q)):
            st.append([st[i][0]-st[i+1][0]*q[i], st[i][1]-st[i+1][1]*q[i]] )
        
        return st[-2]
    else:
        q.append(a//b)
        return extended_gcd(b,a%b)

def mod_exp(a,e,n):
    binary=format(e,'b')
    res=1
    for i in binary:
        res=res**2
        if i=='1': res*=a
        res=res%n
    return res        

def crt(p, q, a, b):   

    c = extended_gcd(p, q) 
    x = a*q*c[1] + b*p*c[0] 
    return x%(p*q)


def crt_list(primes, values):
    a = 1
    res=0
    cnt=1
    for i in primes:
        a *= i
    for i in range(len(primes)):
        cnt=1
        while True:
            if(((a//primes[i])*cnt)%primes[i]==1):
                break
            cnt+=1    
        res+=cnt*a//primes[i]*values[i]
    
    return res%a

print("mod_exp(3,12345,97)=",mod_exp (3, 12345, 97))    
print("mod_exp(3,123456789012345,976)=",mod_exp (3, 123456789012345, 976))


q=[] 
print("crt(10,21,1,2)=",crt(10,21,1,2))
q=[]
print("crt(257,293,11,13)=",crt(257,293,11,13))   

print("crt_list([10,21,29],[1,2,3]=",crt_list([10,21,29],[1,2,3]))
print("crt_list([257,293,337],[11,13,31])=",crt_list ([257, 293, 337], [11, 13, 31]))

