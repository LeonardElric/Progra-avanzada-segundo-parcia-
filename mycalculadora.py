from tkinter import *
global uno,dos,resultado,op

uno=0
dos=0
resultado=0
op="--"

def imprimir1():
    global op,uno,dos
    if(op=="--"):
        uno=10*uno+1
    else:
        dos=10*dos+1
#    print(uno, "\n")
#    print(dos)
def imprimir2():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+2
    else:
        dos=10*dos+2
#    print(uno, "\n")
#    print(dos)
def imprimir3():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+3
    else:
        dos=10*dos+3
#    print(uno, "\n")
#    print(dos)
def imprimir4():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+4
    else:
        dos=10*dos+4
#    print(uno, "\n")
#    print(dos)
def imprimir5():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+5
    else:
        dos=10*dos+5
#    print(uno, "\n")
#    print(dos)
def imprimir6():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+6
    else:
        dos=10*dos+6
#    print(uno, "\n")
#    print(dos)
def imprimir7():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+7
    else:
        dos=10*dos+7
#    print(uno, "\n")
#    print(dos)
def imprimir8():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+8
    else:
        dos=10*dos+8
#    print(uno, "\n")
#    print(dos)
def imprimir9():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+9
    else:
        dos=10*dos+9
#    print(uno, "\n")
#    print(dos)
def imprimir0():
    global op,uno,dos
    if(op=="--"):
        uno=10*uno
    else:
        dos=10*dos
#    print(uno, "\n")
#    print(dos)
def suma():
    global op,uno,dos,resultado
    
    if(op=="suma"):
        resultado=uno+dos
        uno=resultado
    if(op=="resta"):
        resultado=uno-dos
        uno=resultado
    if(op=="multi"):
        resultado=uno*dos
        uno=resultado
    if(op=="div"):
        try:
            resultado=uno/dos
            uno=resultado
        except   ZeroDivisionError:
            print("Ingrese otros numeros")
            
    op="suma"
    dos=0
#    uno=resultado
    
def resta():
    global op,uno,dos,resultado
    
    if(op=="suma"):
        resultado=uno+dos
        uno=resultado
    if(op=="resta"):
        resultado=uno-dos
        uno=resultado
    if(op=="multi"):
        resultado=uno*dos
        uno=resultado
    if(op=="div"):
        try:
            resultado=uno/dos
            uno=resultado
        except   ZeroDivisionError:
            print("Ingrese otros numeros")
            
    op="resta"
    dos=0
#    uno=resultado
    
def multiplicacion():
    global op,uno,dos,resultado
    
    if(op=="suma"):
        resultado=uno+dos
        uno=resultado
    if(op=="resta"):
        resultado=uno-dos
        uno=resultado
    if(op=="multi"):
        resultado=uno*dos
        uno=resultado
    if(op=="div"):
        try:
            resultado=uno/dos
            uno=resultado
        except   ZeroDivisionError:
            print("Ingrese otros numeros")
            
        
    op="multi"
    dos=0
#    uno=resultado
    
def division():
    global op,uno,dos,resultado
    
    if(op=="suma"):
        resultado=uno+dos
        uno=resultado
    if(op=="resta"):
        resultado=uno-dos
        uno=resultado
    if(op=="multi"):
        resultado=uno*dos
        uno=resultado
    if(op=="div"):
        try:
            resultado=uno/dos
            uno=resultado
        except   ZeroDivisionError:
            print("Ingrese otros numeros")
            
            
    op="div"
    dos=0
#    uno=resultado
    
def reset():
    global op,uno,dos,resultado

    pot=0
    uno=0
    dos=0
    resultado=0
    op="--"

def total():
    global resultado,uno,dos,op
    if(dos!=0):
        if(op=="suma"):
            resultado=uno+dos
            uno=resultado
        if(op=="resta"):
            resultado=uno-dos
            uno=resultado
        if(op=="multi"):
            resultado=uno*dos
            uno=resultado
        if(op=="div"):
            try:
                resultado=uno/dos
            except   ZeroDivisionError:
                print("Ingrese otros numeros")
                uno=resultado
        dos=0
        print(resultado)
    else:
        print(resultado)
        uno=resultado
    op="-"
    
ventana=Tk()
texto1=Label(ventana,text="resultado=").grid(column=0,row=0)
texto2=Label(ventana,text=resultado).grid(column=1,row=0)
B1=Button(ventana,text="1",command=imprimir1).grid(column=0,row=1)
B2=Button(ventana,text="2",command=imprimir2).grid(column=1,row=1)
B3=Button(ventana,text="3",command=imprimir3).grid(column=2,row=1)
B4=Button(ventana,text="4",command=imprimir4).grid(column=0,row=2)
B5=Button(ventana,text="5",command=imprimir5).grid(column=1,row=2)
B6=Button(ventana,text="6",command=imprimir6).grid(column=2,row=2)
B7=Button(ventana,text="7",command=imprimir7).grid(column=0,row=3)
B8=Button(ventana,text="8",command=imprimir8).grid(column=1,row=3)
B9=Button(ventana,text="9",command=imprimir9).grid(column=2,row=3)
B0=Button(ventana,text="0",command=imprimir0).grid(column=1,row=4)
BS=Button(ventana,text="+",command=suma).grid(column=0,row=4)
BR=Button(ventana,text="-",command=resta).grid(column=2,row=4)
BM=Button(ventana,text="*",command=multiplicacion).grid(column=4,row=1)
BD=Button(ventana,text="/",command=division).grid(column=4,row=2)
BR=Button(ventana,text="C",command=reset).grid(column=4,row=0)
BI=Button(ventana,text="=",command=total).grid(column=4,row=3)

Liuno=Label(ventana,text="uno").grid(column=6,row=0)
Ltuno=Label(ventana,text=uno).grid(column=7,row=0)

Lidos=Label(ventana,text="dos").grid(column=6,row=1)
Ltdos=Label(ventana,text=dos).grid(column=7,row=1)
ventana.mainloop()

