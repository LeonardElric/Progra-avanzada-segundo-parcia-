from tkinter import *
import random

global posiciones,p,turnos
p=0
turnos=0
posiciones=[0,0,0,0,0,0,0,0,0]

def iniciar():
    global p,turnos,posiciones

    turnos=0
    posiciones=[0,0,0,0,0,0,0,0,0]

    T01.set(" ")
    T02.set(" ")
    T03.set(" ")
    T11.set(" ")
    T12.set(" ")
    T13.set(" ")
    T21.set(" ")
    T22.set(" ")
    T23.set(" ")

    winer.set("--")
    
    a=random.randint(1,2)
    if(a==1):
        player.set("1")
        p=1
    else:
        player.set("2")
        p=2
    Button_play.config(state=DISABLED)
    B00.config(state=NORMAL)
    B01.config(state=NORMAL)
    B02.config(state=NORMAL)
    B10.config(state=NORMAL)
    B11.config(state=NORMAL)
    B12.config(state=NORMAL)
    B20.config(state=NORMAL)
    B21.config(state=NORMAL)
    B22.config(state=NORMAL)
    

def C00():
    global p,posiciones,turnos

    if(p==1):
        posiciones[0]=p
        p=2
        player.set("2")
        T01.set("O")
    else:
        posiciones[0]=p
        p=1
        player.set("1")
        T01.set("X")
    B00.config(state=DISABLED)
    turnos=turnos+1
    search_winer()
    

def C01():
    global p,posiciones,turnos

    if(p==1):
        posiciones[1]=p
        p=2
        player.set("2")
        T02.set("O")
    else:
        posiciones[1]=p
        p=1
        player.set("1")
        T02.set("X")
    B01.config(state=DISABLED)
    turnos=turnos+1
    search_winer()

def C02():
    global p,posiciones,turnos

    if(p==1):
        posiciones[2]=p
        p=2
        player.set("2")
        T03.set("O")
    else:
        posiciones[2]=p
        p=1
        player.set("1")
        T03.set("X")
    B02.config(state=DISABLED)
    turnos=turnos+1
    search_winer()

def C10():
    global p,posiciones,turnos

    if(p==1):
        posiciones[3]=p
        p=2
        player.set("2")
        T11.set("O")
    else:
        posiciones[3]=p
        p=1
        player.set("1")
        T11.set("X")
    B10.config(state=DISABLED)
    turnos=turnos+1
    search_winer()
    

def C11():
    global p,posiciones,turnos

    if(p==1):
        posiciones[4]=p
        p=2
        player.set("2")
        T12.set("O")
    else:
        posiciones[4]=p
        p=1
        player.set("1")
        T12.set("X")
    B11.config(state=DISABLED)
    turnos=turnos+1
    search_winer()

def C12():
    global p,posiciones,turnos

    if(p==1):
        posiciones[5]=p
        p=2
        player.set("2")
        T13.set("O")
    else:
        posiciones[5]=p
        p=1
        player.set("1")
        T13.set("X")
    B12.config(state=DISABLED)
    turnos=turnos+1
    search_winer()

def C20():
    global p,posiciones,turnos

    if(p==1):
        posiciones[6]=p
        p=2
        player.set("2")
        T21.set("O")
    else:
        posiciones[6]=p
        p=1
        player.set("1")
        T21.set("X")
    B20.config(state=DISABLED)
    turnos=turnos+1
    search_winer()
    

def C21():
    global p,posiciones,turnos

    if(p==1):
        posiciones[7]=p
        p=2
        player.set("2")
        T22.set("O")
    else:
        posiciones[7]=p
        p=1
        player.set("1")
        T22.set("X")
    B21.config(state=DISABLED)
    turnos=turnos+1
    search_winer()

def C22():
    global p,posiciones,turnos

    if(p==1):
        posiciones[8]=p
        p=2
        player.set("2")
        T23.set("O")
    else:
        posiciones[8]=p
        p=1
        player.set("1")
        T23.set("X")
    B22.config(state=DISABLED)
    turnos=turnos+1
    search_winer()

def search_winer():
    global posiciones,turnos
    
    if(posiciones[0]==1 and posiciones[1]==1 and posiciones[2]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[3]==posiciones[4]==posiciones[5]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[6]==posiciones[7]==posiciones[8]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[0]==posiciones[3]==posiciones[6]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[1]==posiciones[4]==posiciones[7]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[2]==posiciones[5]==posiciones[8]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[0]==posiciones[4]==posiciones[8]==1):
        winer.set("1")
        lock_buttons()
    if(posiciones[6]==posiciones[4]==posiciones[2]==1):
        winer.set("1")
        lock_buttons()
        
    if(posiciones[0]==posiciones[1]==posiciones[2]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[3]==posiciones[4]==posiciones[5]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[6]==posiciones[7]==posiciones[8]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[0]==posiciones[3]==posiciones[6]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[1]==posiciones[4]==posiciones[7]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[2]==posiciones[5]==posiciones[8]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[0]==posiciones[4]==posiciones[8]==2):
        winer.set("2")
        lock_buttons()
    if(posiciones[6]==posiciones[4]==posiciones[2]==2):
        winer.set("2")
        lock_buttons()
    if(turnos==9):
        winer.set("Empate")
        Button_play.config(state=NORMAL)
#    print(posiciones[0:9])
    
def lock_buttons():
    B00.config(state=DISABLED)
    B01.config(state=DISABLED)
    B02.config(state=DISABLED)
    B10.config(state=DISABLED)
    B11.config(state=DISABLED)
    B12.config(state=DISABLED)
    B20.config(state=DISABLED)
    B21.config(state=DISABLED)
    B22.config(state=DISABLED)
    Button_play.config(state=NORMAL)
    
ventana=Tk()
player=StringVar()
T01=StringVar()
T02=StringVar()
T03=StringVar()
T11=StringVar()
T12=StringVar()
T13=StringVar()
T21=StringVar()
T22=StringVar()
T23=StringVar()
winer=StringVar()

Text_player=Label(ventana,textvariable=player)
Text_player.place(x=100,y=0)
Button_play=Button(ventana,text="comenzar/reiniciar",command=iniciar)
Button_play.place(x=10,y=25)
player_turn=Label(ventana,text="Turno jugador:")
player_turn.place(x=0,y=0)
Txt_winer=Label(ventana,text="ganador: ")
Txt_winer.place(x=125,y=175)
Text_winer=Label(ventana,textvariable=winer)
Text_winer.place(x=175,y=175)

J1=Label(ventana,text="jugador 1: O").place(x=10,y=60)
J2=Label(ventana,text="jugador 2: X").place(x=10,y=80)

B00=Button(ventana,textvariable=T01,command=C00,state=DISABLED)
B00.place(x=10,y=100)
B01=Button(ventana,textvariable=T02,command=C01,state=DISABLED)
B01.place(x=30,y=100)
B02=Button(ventana,textvariable=T03,command=C02,state=DISABLED)
B02.place(x=50,y=100)

B10=Button(ventana,textvariable=T11,command=C10,state=DISABLED)
B10.place(x=10,y=125)
B11=Button(ventana,textvariable=T12,command=C11,state=DISABLED)
B11.place(x=30,y=125)
B12=Button(ventana,textvariable=T13,command=C12,state=DISABLED)
B12.place(x=50,y=125)

B20=Button(ventana,textvariable=T21,command=C20,state=DISABLED)
B20.place(x=10,y=150)
B21=Button(ventana,textvariable=T22,command=C21,state=DISABLED)
B21.place(x=30,y=150)
B22=Button(ventana,textvariable=T23,command=C22,state=DISABLED)
B22.place(x=50,y=150)

ventana.mainloop()
