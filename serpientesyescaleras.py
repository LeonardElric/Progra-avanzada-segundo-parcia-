from tkinter import *
import random

global ini,sel_comienzo,player,pos_act_1,pos_act_2,turnos,winer

sel_comienzo=0
ini=0
D1=0
D2=0
player=0
pos_act_1=0
pos_act_2=0
turnos=0
winer=0

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
        if(player==1 and ini==2 and (winer!=1 or winer!=3)):
            D1=random.randint(1,6)
            pos_act_1=pos_act_1+D1
            if(pos_act_1>=100):
                pos_act_1=100
            avance(player,pos_act_1)
            

        if(player==2 and ini==2 and (winer!=2 or winer!=3)):
            D2=random.randint(1,6)
            pos_act_2=pos_act_2+D2
            if(pos_act_1>=100):
                pos_act_2=100
            avance(player,pos_act_2)
            
    win()
    
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
    global player,ini

    if(jugador==1):
        player=2
        ini=4
        if(posicion<100):
            Avance1.set("Posición jugador 1:\t"+ str(posicion))
        else:
            Avance1.set("El jugador 1 a ganado")
        position(jugador,posicion)
        serpiente_escalera(jugador,posicion)
        Estado_juego.set("Turno del jugador 2")
        
    if(jugador==2):
        player=1
        ini=4
        if(posicion<100):
            Avance2.set("Posición jugador 2:\t"+ str(posicion))
        else:
            Avance2.set("El jugador 2 a ganado")
        position(jugador,posicion)
        serpiente_escalera(jugador,posicion)
        Estado_juego.set("Turno del jugador 1")

def position(etiqueta,pos):
    posx=0
    posy=0
    x=0
    row=0

##    
    if(pos>0):
        posy=530-67*0
        if(pos>=14):
            posy=530-67*1
            if(pos>=27):
                posy=530-67*2
                if(pos>=40):
                    posy=530-67*3
                    if(pos>=53):
                        posy=530-67*4
                        if(pos>=66):
                            posy=530-67*5
                            if(pos>=79):
                                posy=530-67*6
                                if(pos>=92):
                                    posy=530-67*7

    if(pos>0 and pos<=13):
        x=pos
    if(pos>=27 and pos<=40):
        x=pos-26
    if(pos>=53 and pos<=66):
        x=pos-52
    if(pos>=79 and pos<=92):
        x=pos-78
        
    if(pos>13 and pos<=26):
        x=27-pos
    if(pos>39 and pos<=52):
        x=53-pos
    if(pos>65 and pos<=78):
        x=79-pos
    if(pos>91 ):
        x=103-pos
    if(pos>=100):
        x=3

    posx=783-63*(x-1)
                                    
    if(etiqueta==1):
        player1.place(x=posx,y=posy)
        player1.config(bg=("green"))
    if(etiqueta==2):
        player2.place(x=posx,y=posy+20)
        player2.config(bg=("white"))

def serpiente_escalera(jugador,posicion):
    global pos_act_1,pos_act_2
    serpientes=[18,22,36,62,75,78,83,93,96]#9
    dest_serp=[6,2,20,14,30,49,8,40,69]
    escaleras=[11,17,19,21,26,43,52,70,74]#9
    dest_esc=[39,67,45,56,50,84,76,92,100]

    i=0
    
    while(i<9):
        if(posicion==serpientes[i]):
            position(jugador,dest_serp[i])
            if(jugador==1):
                pos_act_1=dest_serp[i]
                serpesc.set("el jugador "+str(jugador)+"\n Descendio por una serpiente a: "+str(dest_serp[i]))
            else:
                pos_act_2=dest_serp[i]
                serpesc.set("el jugador "+str(jugador)+"\n Descendio por una serpiente a: "+str(dest_serp[i]))
        if(posicion==escaleras[i]):                     
            position(jugador,dest_esc[i])
            if(jugador==1):
                pos_act_1=dest_esc[i]
                serpesc.set("el jugador "+str(jugador)+"\n Ascendio por una escalera a: "+str(dest_esc[i]))
            else:
                pos_act_2=dest_esc[i]
                serpesc.set("el jugador "+str(jugador)+"\n Ascendio por una escalera a: "+str(dest_esc[i]))
        i=i+1
            
def win():
    global pos_act_1,pos_act_2,winer

    if(pos_act_1>=100 and winer==0):
        Avance1.set("a ganado el jugador 1")
        winer=1
    if(pos_act_1>=100 and winer==2):
        Avance1.set("a ganado el jugador 1")
        winer=3
        
    if(pos_act_2>=100 and winer==0):
        Avance2.set("a ganado el jugador 2")
        winer=2
    if(pos_act_2>=100 and winer==1):
        Avance2.set("a ganado el jugador 2")
        winer=3
        

def reset():
    global ini,sel_comienzo,player,pos_act_1,pos_act_2,turnos,winer

    sel_comienzo=0
    ini=0
    D1=0
    D2=0
    player=0
    pos_act_1=0
    pos_act_2=0
    turnos=0
    winer=0

    text()

    Avance1.set(" ")
    Avance2.set(" ")
    serpesc.set(" ")
    
ventana=Tk()

ventana.title("serpientes y escaleras")

ventana.geometry("1280x640")

imagen=PhotoImage(file="serps2.png")

img_dado=PhotoImage(file="dado.png")

fondo=Label(ventana,image=imagen).place(x=0,y=0)

Estado_juego=StringVar()

Avance1=StringVar()
Avance2=StringVar()
serpesc=StringVar()

text()

Lest=Label(ventana,textvariable=Estado_juego).place(x=900,y=0)

Lav1=Label(ventana,textvariable=Avance1).place(x=900,y=450)
Lav2=Label(ventana,textvariable=Avance2).place(x=900,y=470)

Lsye=Label(ventana,textvariable=serpesc).place(x=1100,y=460)

dado=Button(ventana,image=img_dado,command=play)
dado.place(x=950,y=55)
BR=Button(ventana,text="Reinicio",command=reset)
BR.place(x=1000,y=350)

player1=Label(ventana,text="J1")
player1.config(bg=("red"))
player2=Label(ventana,text="J2")
player2.config(bg=("blue"))

ventana.mainloop()
