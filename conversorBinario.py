from cgitb import text
from re import sub
import tkinter
from tkinter import END, messagebox

root = tkinter.Tk()
root.title("Conversor decimal a binario")
root.geometry("500x150")
root.resizable(width="false", height="false")


#logica conversion
    #funcion para convertir array a string
def arrToString(arr):
    string=""
    for i in arr:
        string+= str(i)
    return string

#defino funciones que retornen conversion en diferentes sistemas
def convBSS(num,cb):
    if num==0: return "0"
    elif num<0: return "-" # numeros menores que 0 no pueden ser representados en BSS
    else:
        try:
            b=[]
            b= [0 for i in range(cb)]
            i=0
            while num>0:
                d=num%2
                b[i]=d
                num=num//2
                i+=1
            #para devolver como string
            string=arrToString(b)
            return string[::-1] #invierte el string
        except: return "overflow"

def convBCS(num,cb):
    if num>=0: return convBSS(num,cb)
    else:
        try:
            b=[]
            b= [0 for i in range(cb)]
            num*=-1
            i=0
            while num>0:
                d=num%2
                b[i]=d
                num=num//2
                i+=1
            b[-1]=1
            string=arrToString(b)
            return string[::-1]
        except: return "overflow"

def convCA1(num,cb):
    if num>=0: return convBSS(num,cb)
    else:
        try:
            b=[]
            b= [0 for i in range(cb)]
            num*=-1
            i=0
            while num>0:
                d=num%2
                b[i]=d
                num=num//2
                i+=1
            string=arrToString(b)
            string=string[::-1]
            #aplico not al string
            nue=""
            for i in range(cb):
                if int(string[i])==1: nue+="0"
                else: nue+="1"
            return nue
        except: return "overflow"

def convCA2(num,cb):
    if num>=0: return convBSS(num,cb)
    else:
        try:
            b=[]
            b= [0 for i in range(cb)]
            num*=-1
            num-=1 # unica diferencia con ca1, se resta un numero
            i=0
            while num>0:
                d=num%2
                b[i]=d
                num=num//2
                i+=1
            string=arrToString(b)
            string=string[::-1]
            #aplico not al string
            nue=""
            for i in range(cb):
                if int(string[i])==1: nue+="0"
                else: nue+="1"
            return nue
        except: return "overflow"

def convEX2(num,cb):
    exceso=2**(cb-1)
    num+=exceso
    return convBSS(num,cb)

#"Main" de la conversion
def convertir(numero):
    try:
        numero = int(numero)
    except:
        messagebox.showerror("Error", "Por favor, ingrese un numero entero") # si la var numero no es int
    else:   
        try: 
            cantBits = int(bits.get())
        except:
            messagebox.showerror("Error","Por favor, ingrese el numero de bits")
        else:
            #pusheo resultados a los entrys desde la misma funcion
            # binario sin signo: 
            resultadoBSS.config(state='normal')
            resultadoBSS.delete(0,END)
            resultadoBSS.insert(0,convBSS(numero,cantBits))
            resultadoBSS.config(state='readonly')
            # binario con signo:
            resultadoBCS.config(state='normal')
            resultadoBCS.delete(0,END)
            resultadoBCS.insert(0,convBCS(numero,cantBits))
            resultadoBCS.config(state='readonly')
            # complemento a 1
            resultadoCA1.config(state='normal')
            resultadoCA1.delete(0,END)
            resultadoCA1.insert(0,convCA1(numero,cantBits))
            resultadoCA1.config(state='readonly')
            # complemento a 2
            resultadoCA2.config(state='normal')
            resultadoCA2.delete(0,END)
            resultadoCA2.insert(0,convCA2(numero,cantBits))
            resultadoCA2.config(state='readonly')
            # exceso a 2
            resultadoEX2.config(state='normal')
            resultadoEX2.delete(0,END)
            resultadoEX2.insert(0,convEX2(numero,cantBits))
            resultadoEX2.config(state='readonly')
        

#_____________________________________________________________________________________Cuerpo tkinter___________________________________________________________________________________________________________________________#

#input
titulo = tkinter.Label(root, text="Ingresar numero entero:")
titulo.grid(row=0,column= 0)

input = tkinter.Entry(root)
input.grid(row=0,column=1,)

bitsTexto = tkinter.Label(root, text="BITS")
bitsTexto.grid(row=0,column=2)

bits = tkinter.Entry(root)
bits.grid(row=0,column=3,ipadx=3)

boton = tkinter.Button(root, text="Convertir", command= lambda: convertir(input.get()))
boton.grid(row=0,column=4)
#subtitulos con resultados
    #BSS
subindiceBSS = tkinter.Label(root, text="Binario sin signo")
subindiceBSS.grid(row=1,column=0)
resultadoBSS = tkinter.Entry(root)
resultadoBSS.grid(row=1,column=1)
    #BCS
subindiceBCS = tkinter.Label(root, text="Binario con signo")
subindiceBCS.grid(row=2,column=0)
resultadoBCS = tkinter.Entry(root)
resultadoBCS.grid(row=2,column=1)
    #CA1
subindiceCA1 = tkinter.Label(root,text="Complemento a 1")
subindiceCA1.grid(row=3,column=0)
resultadoCA1 = tkinter.Entry(root)
resultadoCA1.grid(row=3,column=1)
    #CA2   
subindiceCA2=tkinter.Label(root,text="Complemento a 2")
subindiceCA2.grid(row=4,column=0)
resultadoCA2 = tkinter.Entry(root)
resultadoCA2.grid(row=4,column=1)
    #EX2
subindiceEX2=tkinter.Label(root,text="Exceso a 2")
subindiceEX2.grid(row=5,column=0)
resultadoEX2= tkinter.Entry(root)
resultadoEX2.grid(row=5,column=1)
root.mainloop()