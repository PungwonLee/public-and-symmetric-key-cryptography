import random
def shift_encrypt(key, msg):
    en= ''
    for i in msg:
       if i<='z'and i>='a':
           en+=chr((ord(i) - 97 + key) % 26 + 97)
       elif i<='Z'and i>='A':
           en+=chr((ord(i) - 65 + key) % 26 + 65)
       else:
           en+=i
    return en    

def shift_decrypt (key, ctx):
    de= ''
    for i in ctx:
       if i<='z'and i>='a':
           de+=chr((ord(i) - 97 - key) % 26 + 97)
       elif i<='Z'and i>='A':
           de+=chr((ord(i) - 65 - key) % 26 + 65)
       else:
           de+=i
    return de       

def vigenere_genkey(n):
    key =''
    for i in range(n):
        key+=chr(random.randrange(97,123))
        
    return key

def vigenere_encrypt(key,msg):
    ven = ''
    for i in range(len(msg)):
        ven += chr((ord(msg[i]) - 97 + (ord(key[i%len(key)])-97) ) % 26 + 97)
    return ven

def vigenere_decrypt(key, ctx):
    vde = ''
    for i in range(len(ctx)):
        vde += chr((ord(ctx[i]) - 97 - (ord(key[i%len(key)])-97) ) % 26 + 97)
    return vde

def lfsr_genkeysteam(n):
    x = []
    y = []
    for i in range(n):
        x.append(random.randrange(0,26))
        y.append(random.randrange(0,26))   # 랜덤한 key 생성
    
    keysteam = (x,y)
    return keysteam

def lfsr_encrypt(key,msg):  
    H = 0
    ctx = ''
    for i in range(len(msg)):
        for j in range(len(key[0])):
            H += key[0][i]*key[1][i+j]
        key[1].append(H%26)
        
    for i in range(len(msg)):
        ctx += chr(((ord(msg[i]) - 97) + key[1][len(key[0])+i]) % 26 + 97) 
    return ctx      
   
    
def lfsr_decrypt(key,ctx):
    H = 0
    lde = ''
    for i in range(len(ctx)):
        for j in range(len(key[0])):
            H += key[0][i]*key[1][i+j]
        key[1].append(H%26)
        
    for i in range(len(ctx)):
        lde +=  chr(((ord(ctx[i]) - 97) - key[1][len(key[0])+i]) % 26 + 97) 
    return lde   

##############################shift
key=int(input("shift 입력: "))                ##shift구간 입력
msg=input("메시지입력: ")                     ##메시지 입력
ct=shift_encrypt(key,msg)
dt=shift_decrypt(key,ct)
print("shift_encrypt:",ct)
print("shift_decrypt:",dt)

##############################vigenere
key=int(input("키 입력: "))                 ## 키 길이 입력
msg=input("메시지입력:")                      ## 메시지 입력
vkey=vigenere_genkey(key)
vct=vigenere_encrypt(vkey,msg)
vdt=vigenere_decrypt(vkey,vct)
print("vigenere_genkey:", vkey)
print("vigenere_encrypt:",vct)
print("vigenere_decrypt:",vdt)

###############################lfsr
key=lfsr_genkeysteam(int(input("키 입력: "))) ## 키 길이 입력
msg=input("메시지입력: ")                          ## 메시지 입력
lct=lfsr_encrypt(key,msg)
ldt=lfsr_decrypt(key,lct)
print("lfsr_encrypt:",lct)
print("lfsr_decrypt:",ldt)
input()
