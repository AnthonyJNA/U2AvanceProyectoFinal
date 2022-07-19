from tkinter import *

def miFuncion():
    print("Registro de un nuevo cliente")

root= Tk ()
root.title("Seguro Leon Dorado")
root.geometry("300x150")
labelPrincipal=Label(root, text="Es cliente nuevo da click en registro")

labelPrincipal.pack()

VentanaSecu= Toplevel(root)
VentanaSecu.geometry("500x300")
Bloque1= Label(VentanaSecu,text="Nombres", bg="red")
Bloque1.place(x=30,y=60,width=100,height=30)
texto1 =  Entry(VentanaSecu, bg="yellow")
texto1.place(x=160,y=60,width=100, height=30)

Bloque2= Label(VentanaSecu,text="Apellidos", bg="red")
Bloque2.place(x=30,y=110,width=100,height=30)
texto2 =  Entry(VentanaSecu, bg="yellow")
texto2.place(x=160,y=110,width=100, height=30)

Bloque3= Label(VentanaSecu,text="Numero de cedula", bg="red")
Bloque3.place(x=30,y=160,width=100,height=30)
texto3 =  Entry(VentanaSecu, bg="yellow")
texto3.place(x=160,y=160,width=100, height=30)

click1=Button(VentanaSecu,text="Registrarse")
click1.place(x=300,y=160,width=80,height=30)
VentanaSecu.title("Registro")

registro=Button(root, text="Registro",bg = "blue",command=miFuncion).pack()

root.mainloop()