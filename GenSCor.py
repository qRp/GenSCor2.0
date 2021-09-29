import tkinter as tk
from langage import L

#variables globales
langue='EN'




#Gestion fenetre tkinter
window=tk.Tk()
#paramètres de la fentre
window.title("GenSCor")
window.minsize(480,480)
#ajout du logo
img=tk.Image("photo", file="genscor.png")
window.tk.call('wm', 'iconphoto', window, img)












#run fenetre principale
window.mainloop()