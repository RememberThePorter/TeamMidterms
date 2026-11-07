y=open('dataset.txt',encoding='utf-8').read().splitlines()
#for i in x:
#    print (i)
x=[]
for i in (y):
    x.append(i.split(","))
def detectlang(s):
    a=[]
    w=[]
    for i in x:
        w=s.split(" ")
        for b in w:
            p=i[0].split(" ")
            if b in p:
                a.append(i[-1])
                #print(b)
    print(a)
    print(w)
    if len(a)!=0:
        print('The language is probably',max(a,key=a.count))
    else:
        print('Word or sentence is not in data set.')

def run():
    
    print('Input any charater from any of these 22 languages:',end=' ')
    s=str(input())
    
    detectlang(s)
    

run()
