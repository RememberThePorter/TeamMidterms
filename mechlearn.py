og=open('dataset.txt',encoding='utf-8').read().splitlines()
#for i in x:
#    print (i)
x=[]

for i in (og):
    x.append(i.split(","))
def detectlang(s):
    a=[]
    w=[]
    for i in x:
        w=s.split(" ")
        for w1 in w:
            w2=i[0].split(" ")
            w1.casefold()
            if w1 in w2:# and len(w1)>2:
                if w1 in ('qwertyuiopasdfghjklzxcvbnm,./;:<>?') and len(w1)<2:
                    continue
                else:
                    a.append(i[-1])
                #print(b)
    print(a)
    print(w)
    if len(a)!=0:
        print('the language is probobly',max(a,key=a.count))
        return(True)
    else:
        print('word or sentence not in data set')
        return(False)

def run():
    og=open('dataset.txt',encoding='utf-8').read().splitlines()
    #for i in x:
    #    print (i)
    x=[]

    for i in (og):
        x.append(i.split(","))
    #print(x[22003])
    print('input any charater from any of these 22 languages:',end=' ')
    s=str(input())
    y=['English','Arabic','French','Hindi','Urdu','Portuguese','Persian','Pushto','Spanish','Korean','Tamil','Turkish','Estonian','Russian','Romanian','Chinese','Swedish','Latin','Indonesian','Dutch','Japanese','Thai']
    z=detectlang(s)
    if z==True:
        flag=True
        while flag==True:
            print('am i correct y or n',end=' ')
            ask=str(input())
            ask.strip()
            ask.casefold()
            if ask== "yes" or ask=="yeah" or ask=="y":
                flag=False
            elif ask== "no" or ask=="nah" or ask=="n":
                right=False
                while right==False:
                    print('what language is it?')
                    for i in range(len(y)):
                        print(i,'=',y[i])
                    try:
                        ans=int(input())
                        with open('dataset.txt','a',encoding='utf-8') as file:
                            file.write('\n'+s+','+y[ans])
                        right=True
                    except:
                        print('please enter a number between 0 and 21')
                    
                flag=False
    else:
        flag=True
        while flag==True:
            print('would you like to add to database',end=' ')
            ask=str(input())
            ask.strip()
            ask.casefold()
            if ask== "yes" or ask=="yeah" or ask=="y":
                right=False
                while right==False:
                    print('what language is it?')
                    for i in range(len(y)):
                        print(i,'=',y[i])
                    try:
                        ans=int(input())
                        with open('dataset.txt','a',encoding='utf-8') as file:
                            file.write('\n'+s+','+y[ans])
                        right=True
                    except:
                        print('please enter a number between 0 and 21')   
                flag=False
            elif ask== "no" or ask=="nah" or ask=="n":
                flag=False
    
    
    

run()
