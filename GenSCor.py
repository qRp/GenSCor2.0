from tkinter.messagebox import *
from tkinter import *
from tkinter.ttk import *
from langage import *
from Variant import *
from Rules import *
from function import *
from Lang import *
from Glob import *
import re
import json
#todo changer les imports pour eviter les wildcards
#create Menu
menubar = Menu(super_window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label=L["Load Rules"][lang], command=preload_rules)
filemenu.add_command(label=L["Load Data"][lang], command=preload_data)
filemenu.insert_separator(index=2)
filemenu.add_command(label=L["Save Rules"][lang], command=prewrite_rules)
filemenu.add_command(label=L["Export Data"][lang], command=preexport_data)
filemenu.insert_separator(index=5)
filemenu.add_command(label=L["Mode non visuel"][lang], command=launch_automode)
filemenu.insert_separator(index=7)
filemenu.add_command(label=L["Parametres"][lang], command=launch_parameters)
filemenu.insert_separator(index=9)
filemenu.add_command(label=L["Quit"][lang], command=tkinter.messagebox.askokcancel)
menubar.add_cascade(label=L["File"][lang], menu=filemenu)
super_window.config(menu=menubar)

#Define maine parameters for the window
super_window.title('GenSCor')
super_window.config(bg='#CEE5D0')


#loading rules and data to test
#load_data('data.tsv')
#load_rules("toto2.json")
#printing all the data and rules to test
#print_all()

#printing the loaded rules and variants on the GUI
print_GUI_rules()
print_GUI_variants()


#main loop
main_window.mainloop()