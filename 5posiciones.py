from tkinter import *
global lab
global actual

actual=12

lab=[]

def inicio():
    global lab,actual

    i=0
    px=0
    py=0
    while(i<25):
        lab.append(Label(matriz,text=" "))
        lab[i].place(x=px,y=py)
        lab[i].config(bg=("white"))

        i=i+1
        px=px+20
        if(px==100):
            px=0
            py=py+20

    lab[actual].config(bg=("red"))

    Button_on.config(state=DISABLED)
    
def reset(mod):
    global lab
    i=0
    while(i<25):
        lab[i].config(bg=("white"))
        i=i+1

    lab[mod].config(bg=("red"))
    
def up():
    global actual

    inc=-5
    
    if(actual!=0 and actual!=1 and actual!=2 and actual!=3 and actual!=4):
        actual=actual+inc
    else:
        actual=20+actual
        
    reset(actual)
        
def down():
    global actual
    
    inc=5

    if(actual!=20 and actual!=21 and actual!=22 and actual!=23 and actual!=24):
        actual=actual+inc
    else:
        actual=actual-20
        
    reset(actual)
    
def right():
    global actual

    inc=1

    if(actual!=4 and actual!=9 and actual!=14 and actual!=19 and actual!=24):
        actual=actual+inc
    else:
        actual=actual-4
        
    reset(actual)
    
def left():
    global actual
    
    inc=-1

    global actual

    inc=1

    if(actual!=0 and actual!=5 and actual!=10 and actual!=15 and actual!=20):
        actual=actual-1
    else:
        actual=actual+4
        
    reset(actual)
    
matriz=Tk()

Button_up=Button(matriz,text="arriba",command=up).place(x=100,y=80)
Button_down=Button(matriz,text="abajo",command=down).place(x=100,y=120)
Button_left=Button(matriz,text="izquierda",command=left).place(x=80,y=100)
Button_right=Button(matriz,text="derecha",command=right).place(x=120,y=100)
Button_on=Button(matriz,text="on",command=inicio)
Button_on.place(x=100,y=100)


matriz.mainloop()
