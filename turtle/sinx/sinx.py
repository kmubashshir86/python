from turtle import*
p=pos()
pu()
goto(129,300)
pd()
write("f(x)=sinx")
goto(p)
width(20)
import math
speed(99999999999)
goto(0,0)
pensize(5)
fd(500)
bk(1000)
write("x-axis")
fd(500)
rt(90)
fd(500)
bk(1000)
fd(500)
lt(90)
pensize(5)
color("Blue")
for i in range(0,1000,3):
    speed(99999999999)
    x=math.sin(math.radians(i))
    fd(2)
    p=pos()
    lt(90)
    pu()
    fd(x*100)
    pd()
    width(4)
    fd(1)
    goto(p)
    rt(90)
   
mainloop()
   
   
   
   
   
