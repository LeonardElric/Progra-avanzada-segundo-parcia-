from tkinter import *
global t_c,c_chicas,c_medianas,c_grandes

def iniciar():
    global t_c,c_chicas,c_medianas,c_grandes

    t_c=0
    c_chicas=0
    c_medianas=0
    c_grandes=0
    estado_banda.set("banda encendida")
    total_cajas.config(state=NORMAL)
    total_cchicas.config(state=NORMAL)
    total_cmed.config(state=NORMAL)
    total_cgrandes.config(state=NORMAL)

    total.set(t_c)
    total_ch.set(c_chicas)
    total_med.set(c_medianas)
    total_gra.set(c_grandes)

    Boton_NB.config(state=NORMAL)
    Boton_Fin.config(state=NORMAL)

def unlock_type():
    global t_c

    t_c=t_c+1
    Boton_NB.config(state=DISABLED)
    Boton_Fin.config(state=DISABLED)
    Boton_CH.config(state=NORMAL)
    Boton_MED.config(state=NORMAL)
    Boton_GR.config(state=NORMAL)
    
def unlock_off():
    Boton_off.config(state=NORMAL)
    
def chica():
    global t_c,c_chicas,c_medianas,c_grandes

    c_chicas=c_chicas+1
    Boton_CH.config(state=DISABLED)
    Boton_MED.config(state=DISABLED)
    Boton_GR.config(state=DISABLED)
    total.set(t_c)
    total_ch.set(c_chicas)

    Boton_NB.config(state=NORMAL)
    Boton_Fin.config(state=NORMAL)
    
def mediana():
    global t_c,c_chicas,c_medianas,c_grandes

    c_medianas=c_medianas+1
    Boton_CH.config(state=DISABLED)
    Boton_MED.config(state=DISABLED)
    Boton_GR.config(state=DISABLED)
    total.set(t_c)
    total_med.set(c_medianas)

    Boton_NB.config(state=NORMAL)
    Boton_Fin.config(state=NORMAL)
    
def grande():
    global t_c,c_chicas,c_medianas,c_grandes

    c_grandes=c_grandes+1
    Boton_CH.config(state=DISABLED)
    Boton_MED.config(state=DISABLED)
    Boton_GR.config(state=DISABLED)
    total.set(t_c)
    total_gra.set(c_grandes)

    Boton_NB.config(state=NORMAL)
    Boton_Fin.config(state=NORMAL)

def reset():
    global t_c,c_chicas,c_medianas,c_grandes

    t_c=0
    c_chicas=0
    c_medianas=0
    c_grandes=0
    estado_banda.set("banda apagada")
    total_cajas.config(state=NORMAL)
    total_cchicas.config(state=NORMAL)
    total_cmed.config(state=NORMAL)
    total_cgrandes.config(state=NORMAL)

    total.set(t_c)
    total_ch.set(c_chicas)
    total_med.set(c_medianas)
    total_gra.set(c_grandes)

    Boton_NB.config(state=DISABLED)
    Boton_Fin.config(state=DISABLED)
    Boton_off.config(state=DISABLED)

ventana=Tk()
ventana.config(width=800,height=900)

Boton_inicio=Button(ventana,text="encender banda",command=iniciar)
Boton_inicio.place(x=10,y=10)
estado_banda=StringVar()
Estado=Label(ventana,textvariable=estado_banda)
Estado.place(x=10,y=40)

total=StringVar()
total_ch=StringVar()
total_med=StringVar()
total_gra=StringVar()
total_cajas=Label(ventana,textvariable=total,state=DISABLED)
total_cajas.place(x=750,y=10)
total_cchicas=Label(ventana,textvariable=total_ch,state=DISABLED)
total_cchicas.place(x=750,y=30)
total_cmed=Label(ventana,textvariable=total_med,state=DISABLED)
total_cmed.place(x=750,y=50)
total_cgrandes=Label(ventana,textvariable=total_gra,state=DISABLED)
total_cgrandes.place(x=750,y=70)

T=Label(ventana,text="Total cajas: ")
TC=Label(ventana,text="Total cajas chicas: ")
TM=Label(ventana,text="Total cajas medianas: ")
TG=Label(ventana,text="Total cajas grandes: ")
T.place(x=550,y=10)
TC.place(x=550,y=30)
TM.place(x=550,y=50)
TG.place(x=550,y=70)

Boton_NB=Button(ventana,text="se ingreso una caja",command=unlock_type,state=DISABLED)
Boton_NB.place(x=50,y=100)
Boton_Fin=Button(ventana,text="Terminar conteo",command=unlock_off,state=DISABLED)
Boton_Fin.place(x=250,y=100)

Size=Label(ventana,text="Tamaño de la caja: ")
Size.place(x=10,y=200)
Boton_CH=Button(ventana,text="chica",command=chica,state=DISABLED)
Boton_CH.place(x=10,y=500)
Boton_MED=Button(ventana,text="mediana",command=mediana,state=DISABLED)
Boton_MED.place(x=100,y=500)
Boton_GR=Button(ventana,text="grande",command=grande,state=DISABLED)
Boton_GR.place(x=200,y=500)


Boton_off=Button(ventana,text="Apagar la banda",command=reset,state=DISABLED)
Boton_off.place(x=400,y=300)

ventana.mainloop()

