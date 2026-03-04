#calling package
import tkinter
import math
e=math.e
pi=math.pi
tau=math.tau

#file handling for color system
def read(x="log.txt"):
    with open(x) as w:
        w.seek(0)
        w=w.read()
    return w

def write(y,x="log.txt"):
    with open(x,'w+') as w:
        w.seek(0)
        w.write(y)
#import time
try:
    L=read()
    L1="blacK"
    if (not bool(L)) or L.upper()=="HELP" or L.upper=="EGG":
        L="light green"
        L1="black"
    elif L.count(",")==1:
        L=L.split(",")
        L,L1=L[0].strip(),L[1].strip()
        if L.upper()==L1.upper():
            if L.upper()=="BLACK":
                L1="white"
            L1="black"
except:
    L="light green"
    L1="black"
        
def root(color=L,fgc=L1):
    def temp_text(df):
        ji.delete(0,'end')
    if color.upper()=="BLACK" or color.upper()=="#000000":
        fgc="white"
    #root
    mi=tkinter.Tk()
    mi.title("logaN=X")
    mi.config(bg=color)
    mi.geometry("365x200")
    mi.maxsize(365,200)


    #entryboxes
    log=tkinter.Label(mi,fg=fgc,bg=color,text="Log")
    log.place(x=50,y=47)

    base=tkinter.Entry(mi,bg=color,fg=fgc)
    base.place(x=80,y=55,width=60,height=20)

    N=tkinter.Entry(mi,bg=color,text='N',fg=fgc)
    N.place(x=145,y=50,width=60)

    og=tkinter.Label(mi,bg=color,text="=",fg=fgc)
    og.place(x=210,y=47)

    ans=tkinter.Entry(mi,bg=color,fg=fgc)
    ans.place(x=230,y=50,width=60)

    def opr():
        try:
            a=base.get()
            n=N.get()
            n=eval(n)
            a=eval(a)
            val=math.log(n,a)
            #val=(n)**(1/eval(a))
            ans.insert(0,val)
        except:
            try:
                if (a==1 or a==0 or a=="0"  or ("-" in a) or (math.copysign(a)==-1)):
                    if n==1:
                        N.delete(0,'end')
                        N.insert(0,"?")
                    elif n=="1":
                        N.delete(0,'end')
                        N.insert(0,"?")
                    base.delete(0,'end')
                    base.insert(0,"?")
                elif a=='1':
                    if n==1:
                        N.delete(0,'end')
                        N.insert(0,"?")
                    elif n=="1":
                        N.delete(0,'end')
                        N.insert(0,"?")
                    base.delete(0,'end')
                    base.insert(0,"?")
                    
                    
                if a==("1" or 1):
                    if n=="":
                        pass
                    else:
                        N.delete(0,'end')
                        N.insert(0,"?")
                    base.delete(0,'end')
                    base.insert(0,"?")
                elif a=="":
                    if n=="":
                        N.delete(0,'end')
                        N.insert(0,"?")
                    N.delete(0,'end')
                    N.insert(0,"?")
                    base.delete(0,'end')
                    base.insert(0,"?")
            except:
                    pass
            try:
                if not a.isnumeric():
                    if not n.isnumeric():
                        N.delete(0,'end')
                        N.insert(0,"?")
                    base.delete(0,'end')
                    base.insert(0,"?")
                elif not n.isnumeric():
                        N.delete(0,'end')
                        N.insert(0,"?")
            except:
                pass
            '''def timer():
                i1=0
                for j in range(1000):
                    i=time.ctime()[17:19]
                    if i[0]=="0":
                        i=int(i[1])
                    else:
                        i=int(i)
                    
                    if j==0:
                        i1=(time.ctime()[17:19])
                        if i1[0]=="0":
                            i1=int(i1[1])
                        else:
                            i1=int(i1)
                    print(i-i1)
                    if i-i1==2:
                        break
                    N.delete(0)
                    base.delete(0)'''
            
    def opr1():
        N.delete(0,"end")
        base.delete(0,"end")
        ji.delete(0,"end")
        ji.insert(0,"color,help")
    but=tkinter.Button(mi,bg=color,text="=",width=2,command=opr,fg=fgc)
    but.place(x=250,y=100,width=40)
    j=tkinter.Button(mi,bg=color,text="RESET",width=2,command=opr1,fg=fgc)
    j.place(x=200,y=100,width=40)
    ji=tkinter.Entry(mi,bg=color,fg=fgc)
    ji.insert(0,"color,help")
    ji.place(x=0,y=0,width=60)
    ji.bind("<FocusIn>",temp_text)
    def dest():
        try:
            OP=ji.get()
            if 1==OP.count(","):
                OPy=OP.split(",")
                a=OPy[0].strip()
                b=OPy[1].strip()
                try:
                    E=tkinter.Entry(bg=a,fg=a)
                    mi.destroy()
                    root(a,b)
                except:
                    OP="lightgreen,black"
                    
            elif OP.upper()=="HELP":
                R=tkinter.Tk()
                R.geometry("200x200")
                R.maxsize(200,200)
                E=tkinter.Text(R)
                E.insert("1.0","logaN=X is a math function created by jhon nappier where a is base, x is argument,(a^X=N) ,base domain=(1,infinity) , log range is R,nearset entry to log is argument and adjascent entry is of argument,and next entry to argument is of answer entry in which answer came on pressing '=' button, 'X' button reset all enteries,topest entry is for color management and help format for color ('background color','text color'),created by mubashsir junior using python tkinter." )
                E.place(x=0,y=0,height=200,width=200)
                R.mainloop()
            elif OP.upper()=="EGG":
                list=['blue','green','yellow','orange','red','black','white','purple','pink','brown','sky blue','turqouise','light green','maroon','grey','silver']
            else:
                try:
                    l=tkinter.Label(bg=OP)
                    mi.destroy()
                    root(OP)
                except:
                    ji.delete(0,"end")
                    ji.insert(0,"color,help")
        except:
            pass
        
        if OP.upper() =="HELP"or OP.upper()=="EGG":
            pass
        else:
            try:
                pk=tkinter.Tk()
                tkinter.Button(pk,fg=OP.split(",")[0])
                tkinter.Button(pk,fg=OP.split(',')[1])
                write(OP)
                pk.destroy()
            except:
                try:
                    pk=tkinter.Tk()
                    tkinter.Button(pk,fg=OP)
                    write(OP)
                    pk.destroy()
                except:
                    pass
            
    jit=tkinter.Button(mi,bg=color,width=2,fg=fgc,text="ok",command=dest)
    jit.place(x=60,y=0,height=20)
    mi.mainloop()
root()

