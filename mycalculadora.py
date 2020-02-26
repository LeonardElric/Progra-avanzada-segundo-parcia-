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
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+1
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir2():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+2
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+2
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir3():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+3
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+3
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir4():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+4
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+4
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir5():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+5
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+5
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir6():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+6
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+6
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir7():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+7
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+7
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir8():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+8
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+8
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir9():
    global op,uno,dos
    if(op=="--"):    
        uno=10*uno+9
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos+9
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
#    print(uno, "\n")
#    print(dos)
def imprimir0():
    global op,uno,dos
    if(op=="--"):
        uno=10*uno
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    else:
        dos=10*dos
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
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
            error=Label(ventana,text="sintax error").grid(column=4,row=0)
            
    op="suma"
    operacion=Label(ventana,text="+").grid(column=1,row=0)
    dos=0
    Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
    texto2=Label(ventana,text=resultado).grid(column=4,row=0)
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
            error=Label(ventana,text="sintax error").grid(column=4,row=0)
            
    op="resta"
    operacion=Label(ventana,text="-").grid(column=1,row=0)
    dos=0
    Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
    texto2=Label(ventana,text=resultado).grid(column=4,row=0)
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
            Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
        except   ZeroDivisionError:
            error=Label(ventana,text="sintax error").grid(column=4,row=0)
            
        
    op="multi"
    operacion=Label(ventana,text="*").grid(column=1,row=0)
    dos=0
    Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
    texto2=Label(ventana,text=resultado).grid(column=4,row=0)
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
            Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
        except   ZeroDivisionError:
            error=Label(ventana,text="sintax error").grid(column=4,row=0)
            
            
    op="div"
    operacion=Label(ventana,text="/").grid(column=1,row=0)
    dos=0
    Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
    texto2=Label(ventana,text=resultado).grid(column=4,row=0)
#    uno=resultado
    
def reset():
    global op,uno,dos,resultado

    pot=0
    uno=0
    dos=0
    resultado=0
    op="--"
    Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
    texto2=Label(ventana,text=resultado).grid(column=4,row=0)

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
                error=Label(ventana,text="sintax error").grid(column=4,row=0)
                uno=resultado
                Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
        dos=0
#        print(resultado)
        Ltdos=Label(ventana,text=dos).grid(column=2,row=0)
    else:
#        print(resultado)
        uno=resultado
        Ltuno=Label(ventana,text=uno).grid(column=0,row=0)
    op="-"
    texto2=Label(ventana,text=resultado).grid(column=4,row=0)
    operacion=Label(ventana,text="+").grid(column=1,row=0)
    
ventana=Tk()
texto1=Label(ventana,text="=").grid(column=3,row=0)
texto2=Label(ventana,text=resultado).grid(column=4,row=0)
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
BR=Button(ventana,text="C",command=reset).grid(column=4,row=4)
BI=Button(ventana,text="=",command=total).grid(column=4,row=3)

#Liuno=Label(ventana,text="uno").grid(column=6,row=0)
Ltuno=Label(ventana,text=uno).grid(column=0,row=0)

#Lidos=Label(ventana,text="dos").grid(column=6,row=1)
Ltdos=Label(ventana,text=dos).grid(column=2,row=0)


ventana.mainloop()

