def gcd(a,b):

    if b==0:
        return a
    else:
        return gcd(b,a%b)

def extended_gcd(a,b):
    if b==0:
        st=[[1,0],[0,1]]
        for i in range(len(q)):
            st.append([st[i][0]-st[i+1][0]*q[i], st[i][1]-st[i+1][1]*q[i]] )
        return a,st[-2][0],st[-2][1]
    else:
        q.append(a//b)
        return extended_gcd(b,a%b)
q=[]
a_e=[[7,15],[666,1428],[1020,10290],[2**20+4,3**10+5],[2**30+1,3**30+6]]
for i in a_e:
    a,b=i
    print("gcd(%d,%d)= %d s= %d t= %d"%(a,b,*extended_gcd(a,b)))
    q=[]
printf(gcd(2**101+16, 2**202+8))
