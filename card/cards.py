op=["♣","♠","♥","♦"]
ap=["A","K","Q","J"]
def push(L,ele):
        global List
        List=L+[ele]
        return List
def pop(List,B=True):
    try:
        a=List[-1]
        if B:
            del List[-1]
        return a
    except:
        return "null"
import pickle
global new
lis=[]
for i in op:
    for j in ap:
        lis.append(j+i)
for i in op:
    for j in range(2,11):
        lis.append(str(j)+i)
import random
new=[]
for i in range(1,14):
    a=(random.choice(lis))
    new.append(a)
    lis.remove(a)
#lis=set(lis)
#new=set(new)
print(new)
print()
   

gk=True
while gk:

    i=input("s\give\save\open\c:").upper()
    if i=="S":
        new.reverse()
        print(new)
    elif i=="EOG":
        print()
        print("cheat activated")
        print()
        new=[]
        l=random.randrange(0,4)
        for i in range(0,4):
            new.append(ap[i]+op[l])
        for i in range(1,11):
            new.append(str(i)+op[l])
        print(new)
        break
    elif i=="LIS":
        print(lis)
    elif i=="C":
        clue=new
        clue=str(clue)
        for i in ap:
            g=clue.count(i)
            if g==13:
                gk=False
            else:
                print("not yet !")
                continue
    elif i=="SAVE":
        with open("save.pkl","wb+") as w:
            w.seek(0)
            pickle.dump(new,w)
            print("if you resave it will overwrite of previous game")
    elif i=="OPEN":
        with open("save.pkl","rb+") as w:
            w.seek(0)
            try:
                new=pickle.load(w)
            except EOFError:
                w.close()
        continue
        
    else:
        try:
            new.remove(i)
            lis=push(lis,i)
            a=random.choice(lis)
            lis.remove(a)
            new=push(new,a)
            print(new)
           
            new=clue                           
            clue=str(clue)
            for i in ap:
                g=clue.count(i)
                if g==13:
                    gk=False
                else:
                    continue
        except:
           continue
          
