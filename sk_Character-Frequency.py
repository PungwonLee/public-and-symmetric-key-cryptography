def char_freq(string):
    char = {}
    for i in string:
        char[i]=0
    for i in string:
        char[i]+=1
    
    print(char)
    return char

def char_freq_file(file):
    S = open(file, mode='r')
    return char_freq(S.read())

def histogram(dict_freq):
    for i in dict_freq.keys():
        print(i, dict_freq[i] * "*" )
        
histogram(char_freq(input()))       #문자열 입력
histogram(char_freq_file(input()))  # 파일 넣을 경로입력
input()
