from tkinter import *
from langage import *
from Variant import *
from Rules import *

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

test=Rules("on",1,"+","Pathogenic","down",50)
print(test.get_value())
print(test.get_type())
print(test.get_sens())
print(test.get_operator())
print(test.get_score_val())
print(test.get_status())
print(test.get_column())