from tkinter import *

window = Tk()
window.title("Calculatrice")
window.geometry("380x500")
window.iconbitmap("calculatrice2.ico")
window.resizable(width=False, height=False)
window.configure(bg='black')

def click3():
    alerte="Erreur !"
    type3 = entrer3.get()
    if type3 == "":
        entrer3.delete(0, END)
        entrer3.insert(0, alerte)
    elif type3 == "Erreur !":
        entrer3.delete(0, END)
        entrer3.insert(0, alerte)
    else:
        entrer3.delete(0, END)
        entrer3.insert(0, eval(type3))

firstext = Label(window, text='Calculatrice', font=("Courier", 30), bg='black')
firstext.config(fg='green')
firstext.pack(pady=20)

entrer3 = Entry(window, font=("Courier", 20), width=20)
entrer3.config(fg='green')
entrer3.pack(pady=10)

button3 = Button(window, text="Calculer", height=2, width=42, command=click3, bg='green')
button3.config(fg='white')
button3.pack(pady=10)

help = Label(window, text='Addition : + \n Soustraction : - \n Multiplication : * \n Division : / \n Puissance : ** \n Modulo : % \n Divison entière : //', font=("Courrier", 13), bg='black')
help.config(fg='green')
help.pack(pady=40)

version = Label(window, text='Version : 1.0.0', font=("Courier", 10), bg='black')
version.config(fg='green')
version.pack(side=BOTTOM)

window.mainloop()