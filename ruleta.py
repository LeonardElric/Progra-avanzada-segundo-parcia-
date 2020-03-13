from tkinter import *
from random import randint
global hacer_apuesta,minimo,din_dis,color
minimo=100
color=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]


def apuesta():
    global hacer_apuesta

    BA=Button(hacer_apuesta,text="Hacer apuesta",command=apuesta_hecha)
    BA.grid(row=6,column=5)

def apuesta_echa():
    global hacer_apuesta

    BAP=Button(ventana,text="Otra apuesta",command=apuesta)
    BAP.grid(row=10,column=10)
    
    hacer_apuesta.withdraw()
    
def comienzo():
    global hacer_apuesta,minimo,din_dis,color, au
    
#    hacer_apuesta.withdraw()
    
    tdin=m.get()
    din_dis=float(tdin)
    hacer_apuesta=Toplevel()
    hacer_apuesta.title("Apuesta")
    hacer_apuesta.withdraw()

    BCR=Button(hacer_apuesta,text="rojos",command=rojos)
    BCR.grid(row=6,column=0)

    BCN=Button(hacer_apuesta,text="negros",command=negros)
    BCN.grid(row=6,column=1)

    BPAR=Button(hacer_apuesta,text="Pares",command=pares)
    BPAR.grid(row=6,column=2)

    BIPR=Button(hacer_apuesta,text="Impares",command=pares)
    BIPR.grid(row=6,column=3)

    BPAS=Button(hacer_apuesta,text="Pasa",command=pasa)
    BPAS.grid(row=6,column=4)

    BFAL=Button(hacer_apuesta,text="Falta",command=falta)
    BFAL.grid(row=6,column=5)

    NUM=Entry(hacer_apuesta,textvariable=au)
    NUM.grid(row=6,column=6)

    BUM=Button(hacer_apuesta,text="verificar numero",command=numero)
    BUM.grid(row=6,column=7)
        
    a=1
    color[0]="verde"

    while(a<=18):
        color[2*a]="negro"
        color[(2*a)-1]="rojo"
        a=a+1
    color[38]="verde"

    if(din_dis<minimo):
        error.set("necesitas mas dinero")
    else:
        error.set("El jugador cuenta con: "+ str(din_dis))
        Brev.config(state=NORMAL)
        Ball.config(state=NORMAL)
        BI.config(state=DISABLED)
        dinero.config(state=DISABLED)
        bienvenido.set("Usted esta jugando")

def verificar():
    global din_dis,minimo

    dr=da.get()

    a=float(dr)

    if(a<=0 and a>din_dis):
        if(a<minimo):
            apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
    if(a>=minimo and a<=din_dis):
        porapostar.set("Usted est apostando: " + str(a))
        BRet=Button(ventana,text="salir",command=fin,state=DISABLED)
        BRet.grid(row=10,column=2)

        Ball.config(state=DISABLED)
        Brev.config(state=DISABLED)
        Dpa.config(state=DISABLED)

        hacer_apuesta.deiconify()
    else:
        apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
        
def todo():
    global din_dis,minimo

    porapostar.set("Usted est apostando: " + str(din_dis))
    BRet=Button(ventana,text="salir",command=fin,state=DISABLED)
    BRet.grid(row=10,column=2)

    Ball.config(state=DISABLED)
    Brev.config(state=DISABLED)
    Dpa.config(state=DISABLED)

    hacer_apuesta.deiconify()

def rojos():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,cont
    x1=1
    x2=3
    x3=5
    x4=7
    x5=9
    x6=11
    x7=13
    x8=15
    x9=17
    x10=19
    x11=21
    x12=23
    x13=25
    x14=27
    x15=29
    x16=31
    x17=33
    x18=35
    cont=1
    comparag()
def negros():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,cont
    x1=2
    x2=4
    x3=6
    x4=8
    x5=10
    x6=12
    x7=14
    x8=16
    x9=18
    x10=20
    x11=22
    x12=24
    x13=26
    x14=28
    x15=30
    x16=32
    x17=34
    x18=36
    cont=2
    comparag()
def pares():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,cont
    x1=2
    x2=4
    x3=6
    x4=8
    x5=10
    x6=12
    x7=14
    x8=16
    x9=18
    x10=20
    x11=22
    x12=24
    x13=26
    x14=28
    x15=30
    x16=32
    x17=34
    x18=36
    cont=2
    comparag()
def impares():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,cont
    x1=1
    x2=3
    x3=5
    x4=7
    x5=9
    x6=11
    x7=13
    x8=15
    x9=17
    x10=19
    x11=21
    x12=23
    x13=25
    x14=27
    x15=29
    x16=31
    x17=33
    x18=35
    cont=1
    comparacion()
def pasa():
    global cont
    cont=3
    comparacion()
              
def fin():
    pass
    
def falta():
    global cont
    cont=4
    comparacion()

def numero():
    global cont
    cont=5
    comparacion()
    
def comparacion():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,cont, au
    skeler=randint(1,37)
    if(skeler!=37):
        if(cont==1):
            if(skeler=x1 or skeler=x2 or skeler=x3 or skeler=x4 or skeler=x5 or skeler=x6 or skeler=x7 or skeler=x8 or skeler=x9 or skeler=x10 or skeler=x11 or skeler=x12 or skeler=x13 or skeler=x14 or skeler=x15 or skeler=x16 or skeler=x17 or skeler=x18)
                #poner lo del apostador
        if(cont==2):
            if(skeler=x1 or skeler=x2 or skeler=x3 or skeler=x4 or skeler=x5 or skeler=x6 or skeler=x7 or skeler=x8 or skeler=x9 or skeler=x10 or skeler=x11 or skeler=x12 or skeler=x13 or skeler=x14 or skeler=x15 or skeler=x16 or skeler=x17 or skeler=x18)
                #lo del ganador
            else:
        if(cont==3):
            if(skeler>18):
                #poner lo del apostador
            else:
        if(cont==4):
            if(skeler<19):
                #poner lo del apostador
             else:
        if(cont==5):
            if(skeler==au):
                #poner lo del apostador
            else:
    else:
        #aqui se pone para si cae 00
ventana=Tk()

m=StringVar()
da=StringVar()
au=StringVar()
error=StringVar()
bienvenido=StringVar()
apostado=StringVar()
porapostar=StringVar()


bienvenido.set("Bienvenido \n La apuesta minima es de: " + str(minimo) + "\n Cuanto dinero tiene?")
dinero=Entry(ventana,textvariable=m)
dinero.grid(row=3,column=2)
BI=Button(ventana,text="ingresar cantidad",command=comienzo)
BI.grid(row=4,column=2)


merror=Label(ventana,textvariable=error)
merror.grid(row=5,column=2)
Lb=Label(ventana,textvariable=bienvenido)
Lb.grid(row=1,column=2)
La=Label(ventana,textvariable=apostado)
La.grid(row=6,column=2)
Lpa=Label(ventana,textvariable=porapostar)
Lpa.grid(row=7,column=2)
Dpa=Entry(ventana,textvariable=da)
Dpa.grid(row=8,column=2)
Brev=Button(ventana,text="Verificar apuesta",command=verificar,state=DISABLED)
Brev.grid(row=9,column=2)
Ball=Button(ventana,text="Apostar todo",command=todo,state=DISABLED)
Ball.grid(row=9,column=3)

    
ventana.mainloop()
