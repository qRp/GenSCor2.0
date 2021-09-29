from tkinter import *
from langage import *
from Variant import *

def fonction_vide():
    x=0

main_window=Tk()
main_window.title('GenSCor')
main_window.config(bg='#CEE5D0')


menubar=Menu(main_window)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=fonction_vide)
menubar.add_cascade(label="File", menu=filemenu)

main_window.config(menu=menubar)
#main_window.mainloop()

test=Variant([1,2,3],10)
print(test.get_Score())
print(test.get_Attributs())
test1=Variant()
print(str(test1.get_Attributs())+"  "+str(test1.get_Score()))