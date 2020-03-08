from tkinter import *
import random

global ini,sel_comienzo,player,pos_act_1,pos_act_2,turnos

sel_comienzo=0
ini=0
D1=0
D2=0
player=0
pos_act_1=0
pos_act_2=0
turnos=0

def text():
    global ini
    
    if(ini==0):
        Estado_juego.set("¿Que jugaror comenzara?" "\n" "Tiren el dado, el jugador que saque el número mayor comenzara" "\n" "Tira el jugador 1")
        
        ini=1

def play():
    global sel_comienzo,D1,D2,player,pos_act_1,pos_act_2,ini

    if(ini==1):
        if(sel_comienzo==1):
            D2=random.randint(1,6)
            sel_comienzo=2

        if(sel_comienzo==2):
            comparar(D1,D2)
        
        if(sel_comienzo==0):
            D1=random.randint(1,6)
            Estado_juego.set("¿Que jugaror comenzara?" "\n" "Tiren el dado, el jugador que saque el número mayor comenzara" "\n" "Tira el jugador 2")
            sel_comienzo=1
    else:
        ini=2
        if(player==1 and ini==2):
            D1=random.randint(1,6)
            pos_act_1=pos_act_1+D1
            player=1
#           Estado_juego.set("Turno del jugador 2" "\n" "Tira el dado")
            avance(player,pos_act_1)

        if(player==2 and ini==2):
            D2=random.randint(1,6)
            pos_act_2=pos_act_2+D2
            player=2
#           Estado_juego.set("Turno del jugador 1" "\n" "Tira el dado")
            avance(player,pos_act_2)

    
def comparar(U,D):
    global sel_comienzo,player,ini

    if(U==D):
        Estado_juego.set("¿Que jugaror comenzara?" "\n" "Tiren el dado de nuevo, el jugador que saque el número mayor comenzara" "\n" "Tira el jugador 1")
        sel_comienzo=0

    if(U>D):
        Estado_juego.set("Comienza el jugador 1" "\n" "Tira el jugador 1")
        ini=2
        player=1
        player1.place(x=850,y=540)
        player2.place(x=850,y=520)

    if(U<D):
        Estado_juego.set("Comienza el jugador 2" "\n" "Tira el jugador 2")
        ini=2
        player=2
        player1.place(x=850,y=540)
        player2.place(x=850,y=520)

def avance(jugador,posicion):
    global pos_act_1,pos_act_2,player,ini

    if(jugador==1):
        player=2
        ini=4
        Estado_juego.set("Turno del jugador 2")
        

    if(jugador==2):
        player=1
        ini=4
        Estado_juego.set("Turno del jugador 1")

def move_pos():
    

ventana=Tk()

ventana.title("serpientes y escaleras")

ventana.geometry("1280x640")

imagen=PhotoImage(file="serps2.png")

img_dado=PhotoImage(file="dado.png")

fondo=Label(ventana,image=imagen).place(x=0,y=0)

Estado_juego=StringVar()

Avance=StringVar()

text()

Lest=Label(ventana,textvariable=Estado_juego).place(x=900,y=0)

Lav=Label(ventana,textvariable=Avance).place(x=900,y=150)

dado=Button(ventana,image=img_dado,command=play)
dado.place(x=950,y=55)

player1=Label(ventana,text="J1")
player1.config(bg=("red"))
player2=Label(ventana,text="J2")
player2.config(bg=("blue"))

ventana.mainloop()
