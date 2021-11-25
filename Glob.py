import datetime
import tkinter

#the list of the rules objects
rules_list=[]
#the list of the variants objects
variants_list=[]
#the header of the loaded data
header_list=[]
#the list of the variables linked to button / option menu etc in the GUI
GUI_var_list=[]
#the list of all the printed items
GUI_item_list=[]
lasttime=datetime.datetime.strptime('22/11/10', '%d/%m/%y')
cool_down=10
Score_name="Score"

#redefine scrolling region of the upper part when the windows is resized
def myfunction_rules(event):
    rules_canvas.configure(scrollregion=rules_canvas.bbox("all"))
#redefine scrolling region of the bottom part when the windows is resized
def myfunction_variants(event):
    variants_canvas.configure(scrollregion=variants_canvas.bbox("all"))

#create the paned window. Upper part is the rule part, bottom part is the variant part.
super_window=tkinter.Tk()
main_window = tkinter.PanedWindow(orient=tkinter.VERTICAL)
main_window.pack(fill=tkinter.BOTH, expand=1)
#adding a super frame in both parts
rules_super_frame = tkinter.Frame(main_window, bg='Red', bd=2, relief="solid")
rules_super_frame.pack(fill="both", expand=True,anchor="n")
variants_super_frame = tkinter.Frame(main_window, bg='Blue', bd=2, relief="solid")
variants_super_frame.pack(fill="both", expand=True,anchor="n")
main_window.add(rules_super_frame)
main_window.add(variants_super_frame)

#We create a canvas in the super frame and a frame in the canvas. This is needed for the scrollbar.
rules_canvas=tkinter.Canvas(rules_super_frame, bg='blue')
rules_frame=tkinter.Frame(rules_canvas, bg='yellow')
#Creating the scrollbar and adding into the superframe for placement purposes, but we link them to the canvas.
myscrollbar_rules=tkinter.Scrollbar(rules_super_frame,orient="vertical",command=rules_canvas.yview)
rules_canvas.configure(yscrollcommand=myscrollbar_rules.set)
myscrollbar_rules.pack(side="right",fill="y")
rules_canvas.pack(side="top",expand=True, fill="both")
rules_canvas.create_window((0,0),window=rules_frame,anchor='nw')
rules_frame.bind("<Configure>",myfunction_rules)

#We create a canvas in the super frame and a frame in the canvas, same as above but for the bottom part.
variants_canvas=tkinter.Canvas(variants_super_frame)
variants_frame=tkinter.Frame(variants_canvas)
#Creating the scrollbar and adding them to the superframe for placement purposes, but we link them to the canvas
myscrollbar_variants_y=tkinter.Scrollbar(variants_super_frame,orient="vertical",command=variants_canvas.yview)
myscrollbar_variants_x=tkinter.Scrollbar(variants_super_frame,orient="horizontal",command=variants_canvas.xview)
variants_canvas.configure(yscrollcommand=myscrollbar_variants_y.set)
variants_canvas.configure(xscrollcommand=myscrollbar_variants_x.set)
myscrollbar_variants_y.pack(side="right",fill="y")
myscrollbar_variants_x.pack(side="bottom",fill="x")
variants_canvas.pack(side="top",expand=True, fill="both")
variants_canvas.create_window((0,0),window=variants_frame,anchor='nw')
variants_frame.bind("<Configure>",myfunction_variants)
