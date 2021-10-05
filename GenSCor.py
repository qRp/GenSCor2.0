from tkinter import *
from langage import *
from Variant import *
from Rules import *
from function import *
import re

def fonction_vide():
    x=0

main_window=Tk()
main_window.title('GenSCor')
main_window.config(bg='#CEE5D0')


menubar=Menu(main_window)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Rules", command=fonction_vide)
filemenu.add_command(label="Load Data", command=fonction_vide)
filemenu.insert_separator(index=2)
filemenu.add_command(label="Save Rules", command=fonction_vide)
filemenu.add_command(label="Export Data", command=fonction_vide)
filemenu.insert_separator(index=5)
filemenu.add_command(label="Quit", command=fonction_vide)

menubar.add_cascade(label="File", menu=filemenu)



rule_test=Rules("on",[1],["="],["Pathogenic"],"up",50)

#test sur les donnees du fichir data
variants_list=[]
f = open("data","r")
lines = f.readlines()
for line in lines:
    data_line=line.split()
    print(data_line)
    variants_list.append(Variant(data_line))



for i in variants_list:
    score_it(rule_test, i)
    print(i.get_Attributs()[0],i.get_Score())



main_window.config(menu=menubar)
#main_window.mainloop()