from tkinter.messagebox import *
from tkinter import *
from tkinter.ttk import *
from langage import *
from Variant import *
from Rules import *
from function import *
from Glob import *
import re
import json

#create Menu
menubar = Menu(main_window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Rules", command=preload_rules)
filemenu.add_command(label="Load Data", command=preload_data)
filemenu.insert_separator(index=2)
filemenu.add_command(label="Save Rules", command=prewrite_rules)
filemenu.add_command(label="Export Data", command=preexport_data)
filemenu.insert_separator(index=5)
filemenu.add_command(label="Quit", command=tkinter.messagebox.askokcancel)
menubar.add_cascade(label="File", menu=filemenu)
main_window.config(menu=menubar)









main_window.title('GenSCor')
main_window.config(bg='#CEE5D0')
main_window.minsize(400,400)

load_rules("toto.json")
load_data('data.tsv')

print_all()

print_GUI_rules()
print(list_possible_values(2))
print(list_possible_values(3))

My_button1=tkinter.Button(main_window, text="Describe_all", command=print_all)
My_button2=tkinter.Button(main_window, text="Score_it", command=score_all)
My_button1.grid(column=5,row=5)
My_button2.grid(column=5,row=6)


main_window.mainloop()