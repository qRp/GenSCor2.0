import tkinter

rules_list=[]
variants_list=[]
header_list=[]
GUI_var_list=[]
GUI_item_list=[]


def myfunction_rules(event):
    rules_canvas.configure(scrollregion=rules_canvas.bbox("all"))

def myfunction_variants(event):
    variants_canvas.configure(scrollregion=variants_canvas.bbox("all"))


super_window=tkinter.Tk()
main_window = tkinter.PanedWindow(orient=tkinter.VERTICAL)
main_window.pack(fill=tkinter.BOTH, expand=1)
rules_super_frame = tkinter.Frame(main_window, bg='Red', bd=2, relief="solid")
rules_super_frame.pack(fill="both", expand=True,anchor="n")
variants_super_frame = tkinter.Frame(main_window, bg='Blue', bd=2, relief="solid")
variants_super_frame.pack(fill="both", expand=True,anchor="n")
main_window.add(rules_super_frame)
main_window.add(variants_super_frame)


rules_canvas=tkinter.Canvas(rules_super_frame, bg='blue')
rules_frame=tkinter.Frame(rules_canvas, bg='yellow')
myscrollbar_rules=tkinter.Scrollbar(rules_super_frame,orient="vertical",command=rules_canvas.yview)
rules_canvas.configure(yscrollcommand=myscrollbar_rules.set)
myscrollbar_rules.pack(side="right",fill="y")
rules_canvas.pack(side="top",expand=True, fill="both")
rules_canvas.create_window((0,0),window=rules_frame,anchor='nw')
rules_frame.bind("<Configure>",myfunction_rules)

variants_canvas=tkinter.Canvas(variants_super_frame)
variants_frame=tkinter.Frame(variants_canvas)
myscrollbar_variants_y=tkinter.Scrollbar(variants_super_frame,orient="vertical",command=variants_canvas.yview)
myscrollbar_variants_x=tkinter.Scrollbar(variants_super_frame,orient="horizontal",command=variants_canvas.xview)
variants_canvas.configure(yscrollcommand=myscrollbar_variants_y.set)
variants_canvas.configure(xscrollcommand=myscrollbar_variants_x.set)
myscrollbar_variants_y.pack(side="right",fill="y")
myscrollbar_variants_x.pack(side="bottom",fill="x")
variants_canvas.pack(side="top",expand=True, fill="both")
variants_canvas.create_window((0,0),window=variants_frame,anchor='nw')
variants_frame.bind("<Configure>",myfunction_variants)
