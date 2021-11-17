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
#todo changer les imports pour eviter les wildcards

#create Menu
menubar = Menu(super_window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Rules", command=preload_rules)
filemenu.add_command(label="Load Data", command=preload_data)
filemenu.insert_separator(index=2)
filemenu.add_command(label="Save Rules", command=prewrite_rules)
filemenu.add_command(label="Export Data", command=preexport_data)
filemenu.insert_separator(index=5)
filemenu.add_command(label="Mode non visuel", command=launch_automode)
filemenu.insert_separator(index=7)
filemenu.add_command(label="Quit", command=tkinter.messagebox.askokcancel)
menubar.add_cascade(label="File", menu=filemenu)
super_window.config(menu=menubar)

#Define maine parameters for the window
super_window.title('GenSCor')
super_window.config(bg='#CEE5D0')


#loading rules and data to test
load_rules("toto.json")
load_data('data.tsv')
#printing all the data and rules to test
print_all()

#printing the loaded rules and variants on the GUI
print_GUI_rules()
print_GUI_variants()


#main loop
main_window.mainloop()