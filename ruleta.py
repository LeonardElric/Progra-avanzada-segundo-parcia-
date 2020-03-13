from tkinter import *
from random import randint
global hacer_apuesta,minimo,din_dis,color
minimo=100
color=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]


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
    global hacer_apuesta,minimo,din_dis,color
    
#    hacer_apuesta.withdraw()
    
    tdin=m.get()
    din_dis=float(tdin)

    a=1
    color[0]="verde"

    while(a<=18):
        color[2*a]="negro"
        color[(2*a)-1]="rojo"
        a=a+1

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

    if(a<=0 and a>din_dis and a<minimo):
        apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
    else:
        hacer_apuesta=Toplevel()
        hacer_apuesta.title("Apuesta")
        porapostar.set("Usted est apostando: " + str(a))
        BRet=Button(ventana,text="salir",command=fin,state=DISABLED)
        BRet.grid(row=10,column=2)

        Ball.config(state=DISABLED)
        Brev.config(state=DISABLED)
        Dpa.config(state=DISABLED)
        
def todo():
    pass

def fin():
    pass
        
ventana=Tk()

m=StringVar()
da=StringVar()
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

##hacer_apuesta=Toplevel()
##        hacer_apuesta.title("Apuesta")
##        BI.config(state=DISABLED)
##        dinero.config(state=DISABLED)
##        bienvenido.set("Usted esta jugando")
##        BRet=Button(ventana,text="salir",command=fin,state=DISABLED)
