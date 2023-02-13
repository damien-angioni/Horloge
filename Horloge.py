from tkinter import *			
from time import *
vartype=True
def horaire():
    if vartype==True:
        Label_temps.config(text=strftime("%H:%M:%S"))
    else:
        Label_temps.config(text=strftime("%I:%M %p"))
    Label_temps.after(200, horaire)
def choix(choisit):
    global vartype
    vartype = choisit
#Fonction principale
fenetre = Tk()
fenetre.resizable(width=False, height=False) 
fenetre.geometry("118x55")
fenetre.config(bg="white") 
Label_temps = Label(fenetre, font=(20), bg='white') 
Label_temps.grid(row=1, column=1, columnspan=2)
horaire()
btn24 = Button(fenetre, text ="form 24h", command = lambda: choix(True))
btn24.grid(row=2, column=1)
btn12 = Button(fenetre, text ="form 12h", command = lambda: choix(False))
btn12.grid(row=2, column=2)
fenetre.mainloop()