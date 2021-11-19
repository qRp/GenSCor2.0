import re
import tkinter
import tkinter.ttk
import tkinter.filedialog
from Rules import *
from Variant import *
from Glob import *
import json

#Calculate the score for all the variants with every rules
def score_all():
    print("Début score")
    global rules_list, variants_list
    #for each variants in the list, we reset the score
    for i in variants_list:
        i.set_Score(0)
    #for each rule in the list
    for i in rules_list:
        #if the rule is active, we use it on every variants
        if i.get_status() == "on":
             for j in variants_list:
                score_it(i,j)
    #actualising the GUI
    print_GUI_variants()

#calculate the score for one variant with one rule
def score_it(rule, variant):
    to_return = 0
    #rule.describe()
    #variant.describe()
    #for each condition of the rule
    for i in range(len(rule.get_column())):
        working_value = variant.get_one_attribut(int(rule.get_one_column(i)))
        #testing the condition on the variant
        result = compare(working_value, rule.get_one_operator(i), rule.get_one_value(i))
        #if the condition is true, we add 1
        if result:
            to_return+=1
    #if all the conditions are true, we update the score
    if to_return == len(rule.get_column()):
        if rule.get_sens() == "up":
            variant.set_Score(variant.get_Score() + float(rule.get_score_val()))
        elif rule.get_sens() == "down":
            variant.set_Score(variant.get_Score() - float(rule.get_score_val()))
    else:
        return False

#function to check if a condition is true on a variant
def compare(working_value, operator, value):
    #print("comparaison :"+str(working_value)+" "+str(operator)+" "+str(value))
    #encapsulate to handle type problems. For each possible operator, we test the condition and return the according result.
    try :
        if operator == ">" :
            if float(working_value) > float(value) :
                return True
            else :
                return False
        elif operator == ">=" :
            if float(working_value) >= float(value) :
                return True
            else :
                return False

        elif operator == "<" :
            if float(working_value) < float(value) :
                return True
            else :
                return False

        elif operator == "<=":
            if float(working_value) <= float(value) :
                return True
            else :
                return False

        elif operator == "=":
            if float(working_value) == float(value) :
                return True
            else :
                return False

        elif operator == "!=":
            if float(working_value) != float(value) :
                return True
            else :
                return False

        elif operator == "match":
            if re.match(str(working_value), str(value)) :
                return True
            else :
                return False

        elif operator == "contain":
            if str(working_value) in str(value):
                return True
            else:
                return False
        elif operator == "don't contain":
            if str(working_value) not in str(value):
                return True
            else:
                return False
    except TypeError:
        print("Le type de donnée n'est pas adapté à l'opérateur")
        return False
    except ValueError:
        print("Le type de donnée n'est pas adapté à l'opérateur")

    #convert the rule to a json string for saving.
def convert_to_json(rule):
    global header_list
    size_list=len(rule.get_column())
    my_json='{"Status": "'+rule.get_status()+'","TextColumn": ['
    cpt=0
    for i in rule.get_textcolumn():
        cpt+=1
        my_json=my_json+'"'+str(i)+'"'
        if cpt < size_list:
            my_json=my_json+','
        else :
            my_json=my_json+'], "Operator": ['
    cpt=0
    for i in rule.get_operator():
        cpt+=1
        my_json=my_json+'"'+str(i)+'"'
        if cpt < size_list:
            my_json=my_json+','
        else :
            my_json=my_json+'], "Value": ['
    cpt=0
    for i in rule.get_value():
        cpt+=1
        my_json=my_json+'"'+str(i)+'"'
        if cpt < size_list:
            my_json=my_json+','
        else :
            my_json=my_json+'], "Sens":"'
    my_json = my_json+rule.get_sens()+'","Score_val": "'+str(rule.get_score_val())+'"}'
    return my_json

def header_index_to_string(index):
    print(index)
    print(header_list)
    return header_list[index]

def header_string_to_index(string):
    print(header_list)
    return header_list.index(string)

def header_update():
    global rules_list
    for rule in rules_list:
        text_column_list=rule.get_textcolumn()
        for i in range(len(text_column_list)):
            text_column=rule.get_one_textcolumn(i)
            index=header_list.index(text_column)
            rule.set_one_column(index, i)



#load data from file
def load_data(file_path):
    global variants_list, header_list
    #reset the variants_list
    variants_list=[]
    #opening and reading the file
    f = open(file_path, "r")
    lines = f.readlines()
    #if there is a header
    header_is_set=False
    for line in lines:
        data_line = line.split()
        #updating the header and not putting it into the variants list
        if header_is_set == False:
            header_list=data_line
            header_update()
            header_is_set=True
        else :
            #if it is not a header line, adding to the list of variants
            variants_list.append(Variant(data_line))

#writing data into file
def export_data(file_path):
    global variants_list
    #openning and writing the score for each variant
    f = open(file_path, "w")
    for i in variants_list:
        f.write(str(i.get_Score())+"\t")
        #and writing every attributes for each variant
        for j in i.get_Attributs():
            f.write(j+"\t")
        f.write("\n")

#writing rules into file
def write_rules(file_path):
    global rules_list
    #openning of the file
    f = open(file_path, "w")
    f.write('{"rules":\n')
    #for each rules, we convert it into json format and write the resulting string into file
    for i in rules_list:
        i.describe()
        rule_json=convert_to_json(i)
        f.write(rule_json+"\n")
    f.write('}')

#loading rules from file
def load_rules(file_path):
    global rules_list, header_list
    #openning and reading
    rules_list=[]
    f = open(file_path, "r")
    lines=f.readlines()
    #for each line, extract rule info. The expected format is json.
    for line in lines:
        try :
            jdict=json.loads(line)
            Columns=[]
            #if there is a header defined, we directly set the column index
            for i in jdict["TextColumn"]:
                if len(header_list)!=0:
                    Columns.append(i)
                #else, we initialise with 0, waiting for data to be loaded
                else:
                    Columns.append(0)
            rule=Rules(jdict["Status"],jdict["Column"],jdict["Operator"],jdict["Value"],jdict["Sens"], jdict["Score_val"], jdict["TextColumn"])
            rules_list.append(rule)
        #if the line is not in json format, we do nothing
        except :
            pass


#function triggered before loading rules from file. Ask the user where is the file to load.
def preload_rules():
    file=tkinter.filedialog.askopenfilename(filetypes =[('Json Files', '*.json'),('All Files', '*')])
    if file is not None:
        load_rules(file)
    else :
        return 1

#function triggered before loading variants from file. Ask the user where is the file to load.
def preload_data():
    global header_list
    file=tkinter.filedialog.askopenfilename(filetypes=[('txt Files', '*.txt'),('tsv Files', '*.tsv'),('All Files', '*')])
    if file is not None:
        load_data(file)
    else:
        return 1

#function triggered before writing rules from file. Ask the user where is the file to write into.
def prewrite_rules():
    file=tkinter.filedialog.asksaveasfilename(filetypes=[('json Files', '*.json'),('All Files', '*')], defaultextension=".json")
    if file is not None:
        write_rules(file)
    else:
        return 1

#function triggered before writing data rules from file. Ask the user where is the file to write into.
def preexport_data():
    file=tkinter.filedialog.asksaveasfilename(filetypes=[('tsv Files', '*.tsv'),('txt Files', '*.txt'),('All Files', '*')],defaultextension=".tsv")
    if file is not None:
        export_data(file)
    else:
        return 1

#launch the no visual mode for autoscoring multiples files
def launch_automode():
    #list of filenames
    data_file_list=()
    rules_file_list=()
    #nested function to update the list of filenames with a dialog box
    def select_data():
        nonlocal data_file_list
        files=tkinter.filedialog.askopenfilenames(filetypes=[('tsv Files', '*.tsv'),('txt Files', '*.txt'),('All Files', '*')]
                                                  ,defaultextension=".tsv")
        #if there is file selected, we update the list
        if len(files)!=0:
            data_file_list=files
            #and we update the GUI to print the selected files
            update_GUI_no_visual()
        else:
            return None
    #nested function to update the list of data filenames with a dialog box
    def select_rules():
        nonlocal rules_file_list
        files = tkinter.filedialog.askopenfilenames(filetypes=[('json Files', '*.json'), ('All Files', '*')],
                                                    defaultextension=".json")
        #if some files are selected
        if len(files)!=0:
            rules_file_list=files
            #updating the GUI to print the selected filepath
            update_GUI_no_visual()
        else:
            return None

    #Calculate the score for all the combinaison rules / Variants
    def calculate():
        for data_file in data_file_list:
            load_data(data_file)
            for rule_file in rules_file_list:
                load_rules(rule_file)
                score_all()
                export_data()

    #all the items of the GUI
    def update_GUI_no_visual():
        #We start by removing everything
        for i in (automode_windows.winfo_children()):
            i.destroy()
        #we create three buttons : one for the rules, one for the variant and one for the scoring
        select_data_button = tkinter.Button(automode_windows, text="Select data", command=select_data)
        select_rules_button = tkinter.Button(automode_windows, text="Select Rules", command=select_rules)
        score_all_button=tkinter.Button(automode_windows, text="Calculer le score", command=calculate)
        #griding the first button
        select_data_button.grid(column=1, row=0)
        #gridding the score button only if there is rules AND data selected
        if len(rules_file_list) !=0 and len(data_file_list) !=0 :
            score_all_button.grid(column=2, row=0)
        #gridding the last one
        select_rules_button.grid(column=3, row=0)
        cpt=0
        #for each data filepath selected, printing it in a label
        for i in data_file_list :
            cpt+=1
            data_label=tkinter.Label(automode_windows, text=i)
            data_label.grid(column=1, row=cpt)
        cpt=0
        #for each rules filepath selected, printing it in a label
        for i in rules_file_list :
            cpt+=1
            rule_label=tkinter.Label(automode_windows, text=i)
            rule_label.grid(column=3, row=cpt)

    #Window creation and resizing
    automode_windows=tkinter.Tk()
    automode_windows.title('Automode')
    automode_windows.geometry('310x110')
    update_GUI_no_visual()
    automode_windows.mainloop()


#create a rule
def create_rule():
    global rules_list
    new_rule=Rules()
    rules_list.append(new_rule)
    # remove everything on the GUI
    for i in (rules_frame.winfo_children()):
        i.destroy()
    #Updating the GUI, we need to destroy the button may be duplicate otherwise
    print_GUI_rules()

#copy and paste a rule.
def dupliquate_rule(rule):
        global rules_list
        #getting all the info of the mother rule
        status=rule.get_status()
        column=rule.get_column()
        operator=rule.get_operator()
        sens=rule.get_sens()
        value=rule.get_value()
        score_val=rule.get_score_val()
        #creating the daughter rule with the same infos
        rule = Rules(status, column, operator, value, sens, score_val)
        #adding the rule to the list
        rules_list.append(rule)
        # remove everything on the GUI
        for i in (rules_frame.winfo_children()):
            i.destroy()
        #and updating the GUI
        print_GUI_rules()

#remove a rule
def delete_rule(index):
    global rules_list
    #remove the rule from the list
    rules_list.pop(index)
    #remove everything on the GUI
    for i in (rules_frame.winfo_children()):
        i.destroy()
    #and recreating the GUI
    print_GUI_rules()


#copy and paste a condition.
def dupliquate_condition(i, j):
        global rules_list
        #getting the number of conditions at this point.
        size=len(i.get_column())
        #getting the same values that the condition to copy
        operator=i.get_one_operator(j)
        value=i.get_one_value(j)
        column=i.get_one_column(j)
        #pasting into a new condition
        i.set_one_value(value, size)
        i.set_one_column(column, size)
        i.set_one_text_column(header_list[column], size)
        i.set_one_operator(operator, size)
        # remove everything on the GUI because we must shift all widgets
        for i in (rules_frame.winfo_children()):
            i.destroy()
        #and updating the GUI
        print_GUI_rules()

#remove a condition
def delete_condition(index, j):
    global rules_list
    rule=rules_list[index]
    rule.remove_one_value(j)
    rule.remove_one_operator(j)
    rule.remove_one_column(j)
    #if the rule is empty
    if len(rule.get_column())==0:
        delete_rule(index)
    else:
       #remove everything on the GUI
       for i in (rules_frame.winfo_children()):
           i.destroy()
       #and recreating the GUI
       print_GUI_rules()



#print everything into the log console. Used for debug purposes.
def print_all():
    global variants_list, rules_list
    print("Describe all :")
    #print everything about the variants
    for i in variants_list:
        i.describe()
    #print everything about the rules
    for i in rules_list:
        i.describe()

#Get all the possible values in a column of data
def list_possible_values(index):
    list_of_values={}
    return_list=[]
    #for each variants in the list, we are looking the value in the column of interest and adding it to a dictionnary
    for i in variants_list:
        list_of_values[i.get_one_attribut(index)]=1
    #for each different value, adding it to the return list
    for i in list_of_values.keys():
        return_list.append(i)
    #and returning the list
    return return_list

def print_GUI_rules():
    global rules_list,GUI_var_list, GUI_item_list
    column_start = 3
    #initialisation de la liste de dictionnaire ou sont stockés les boutons
    GUI_var_list = [dict() for x in range(len(rules_list))]
    GUI_item_list = [dict() for x in range(len(rules_list))]
    cpt=0
    index=0
    for i in rules_list:
        cpt=print_rule(i,index,cpt, column_start)
        cpt+=1
        index+=1
    # Create button for test purposes
    My_button1 = tkinter.Button(rules_frame, text="Describe_all", command=print_all)
    My_button2 = tkinter.Button(rules_frame, text="Score_it", command=score_all)
    My_button1.grid(column=column_start+2, row=cpt+1)
    My_button2.grid(column=column_start+1, row=cpt+1)
    #Create button for adding a new rule
    Add_button = tkinter.Button(rules_frame, text="Add new rule", command=lambda: create_rule())
    Add_button.grid(column=column_start, row=cpt+1)


def print_rule(i,index,cpt, column_start):
    global GUI_var_list, header_list, GUI_item_list
    style_on = {'bg': '#CEE5D0', 'font':"-overstrike 0"}
    style_off = {'bg': 'grey', 'font': "-overstrike 1"}

    def update_GUI(style_actif):
        dupliquer_button.configure(style_actif)
        delete_button.configure(style_actif)
        status_button.configure(style_actif)
        text_label1.configure(style_actif)
        sens_optionmenu.configure(style_actif)
        text_label2.configure(style_actif)
        text_label3.configure(style_actif)

    def updated_status(i):
        if i.get_status() == "on":
            i.set_status("off")
            style_actif=style_off
        else:
            i.set_status("on")
            style_actif=style_on
        update_GUI(style_actif)
        i.describe()

    def updated_sens(i,index):
        print("Update sens")
        i.set_sens(GUI_var_list[index]["sens"].get())
        score_all()
        i.describe()

    def updated_score_val(value, rule):
        print("Update score val")
        rule.set_score_val(value.get())
        score_all()
        rule.describe()

    def updated_column(new_value, i, index, j):
        print("Update column !")
        new_column_index=header_list.index(GUI_var_list[index]["column"][int(j)].get())
        i.set_one_column(new_column_index,j)
        i.set_one_text_column(header_list[new_column_index], j)
        GUI_item_list[index]["combobox_value"][j]['values'] = list_possible_values(int(i.get_one_column(j)))
        GUI_item_list[index]["combobox_value"][j].set(GUI_item_list[index]["combobox_value"][j]['values'][0])
        i.set_one_value(GUI_item_list[index]["combobox_value"][j]['values'][0], j)
        score_all()
        i.describe()

    def updated_operator(i, index, j):
        print("Update operator !")
        i.set_one_operator(GUI_var_list[index]["operator"][int(j)].get(),j)
        score_all()
        i.describe()

    def updated_value(event, i, index, j):
        print("Update value !")
        i.set_one_value(GUI_var_list[index]["value"][j].get(),j)
        score_all()
        i.describe()

    #creation du bouton Mute
    status_button = tkinter.Button(rules_frame, text="Mute", command=lambda index=index, i=i: updated_status(i,index))
    if i.get_status() == "on":
        style_actif=style_on
    else:
        style_actif=style_off
    status_button.configure(style_actif)
    status_button.grid(column=column_start+1, row=cpt)

    #creation du bouton Dupliquer
    dupliquer_button = tkinter.Button(rules_frame, text="Dup", command=lambda i=i: dupliquate_rule(i))
    dupliquer_button.grid(column=column_start-1, row=cpt)
    dupliquer_button.configure(style_actif)

    #creation du bouton Delete
    delete_button = tkinter.Button(rules_frame, text="Sup", command=lambda index=index: delete_rule(index))
    delete_button.grid(column=column_start, row=cpt)
    delete_button.configure(style_actif)
    #Creation du premier label
    text_label1 = tkinter.Label(rules_frame, text="Si toutes ces conditions sont vrais, le score va")
    text_label1.configure(style_actif)
    text_label1.grid(column=column_start+2, row=cpt)

    #Creation de l'option menu sens
    option_sens = ["up", "down"]
    option_sens_var=tkinter.StringVar()
    GUI_var_list[index]["sens"] = option_sens_var
    GUI_var_list[index]["sens"].set(i.get_sens())
    sens_optionmenu = tkinter.OptionMenu(rules_frame, option_sens_var, *option_sens,
                                    command=lambda new_value, index=index, i=i: updated_sens(i,index))
    sens_optionmenu.configure(style_actif)
    sens_optionmenu.grid(column=column_start+3, row=cpt)

    #Creation du deuxième label
    text_label2 = tkinter.Label(rules_frame, text=" de ")
    text_label2.configure(style_actif)
    text_label2.grid(column=column_start+4, row=cpt)
    #creation du champs score value
    GUI_var_list[index]["score_value"]=tkinter.StringVar()
    GUI_var_list[index]["score_value"].set(i.get_score_val())
    GUI_var_list[index]["score_value"].trace("w", lambda name, index, mode,
                            value=GUI_var_list[index]["score_value"],rule=i: updated_score_val(value, rule))
    score_value_entry = tkinter.Entry(rules_frame, textvariable=GUI_var_list[index]["score_value"])
    score_value_entry.grid(column=column_start+5, row=cpt)

    #creation du troisieme label
    text_label3 = tkinter.Label(rules_frame, text=" point(s).")
    text_label3.configure(style_actif)
    text_label3.grid(column=column_start+6, row=cpt)
    #retour à la ligne et boucle sur les conditions

    GUI_var_list[index]["column"] = {}
    GUI_var_list[index]["operator"] = {}
    GUI_var_list[index]["value"] = {}
    GUI_item_list[index]["combobox_value"]={}
    for j in range(len(i.get_column())):
        cpt += 1
        # creation du bouton Dupliquer
        dupliquer_button = tkinter.Button(rules_frame, text="Dup", command=lambda i=i: dupliquate_condition(i, j))
        dupliquer_button.grid(column=column_start + 1, row=cpt)
        dupliquer_button.configure(style_actif)

        # creation du bouton Delete
        delete_button = tkinter.Button(rules_frame, text="Sup", command=lambda index=index: delete_condition(index, j))
        delete_button.grid(column=column_start, row=cpt)
        delete_button.configure(style_actif)

        #affichage des optionmenu colonnes
        column_var = tkinter.StringVar()
        GUI_var_list[index]["column"][j] = column_var
        GUI_var_list[index]["column"][j].set(header_list[int(i.get_one_column(j))])
        column_optionmenu = tkinter.OptionMenu(rules_frame, GUI_var_list[index]["column"][j],*header_list,
                                               command= lambda new_value, index=index, i=i, j=j: updated_column(new_value, i,index, j))
        column_optionmenu.grid(column=column_start+2, row=cpt)

        #affichage des optionmenu colonnes
        operator_var = tkinter.StringVar()
        GUI_var_list[index]["operator"][j] = operator_var
        GUI_var_list[index]["operator"][j].set(i.get_one_operator(j))
        operator_values=["=", "!=", "<", "<=", ">", ">=", "match", "contain", "don't contain"]
        operator_optionmenu = tkinter.OptionMenu(rules_frame, GUI_var_list[index]["operator"][j],*operator_values,
                                               command= lambda new_value, index=index, i=i, j=j: updated_operator(i,index, j))
        operator_optionmenu.grid(column=column_start+3, row=cpt)
        #value combobox
        value_var=tkinter.StringVar()
        GUI_var_list[index]["value"][j] = value_var
        GUI_item_list[index]["combobox_value"][j]=tkinter.ttk.Combobox(rules_frame, textvariable=GUI_var_list[index]["value"][j])
        GUI_item_list[index]["combobox_value"][j]['values'] = list_possible_values(int(i.get_one_column(j)))
        GUI_item_list[index]["combobox_value"][j].bind("<<ComboboxSelected>>", lambda event, i=i, index=index, j=j : updated_value(event, i, index, j))
        GUI_item_list[index]["combobox_value"][j].set(i.get_one_value(j))
        GUI_item_list[index]["combobox_value"][j].grid(column=column_start+4, row=cpt)
    return cpt


def print_GUI_variants():
    #todo trier variants, ajouter header, ajouter score, update score, afficher que top 10 premiers, naviguation variants suivants
    #remove everything on the GUI
    for i in (variants_frame.winfo_children()):
        i.destroy()
    cpt_y=0
    for i in variants_list:
        cpt_y+=1
        cpt_x=0
        score_label=tkinter.Label(variants_frame, text=i.get_Score())
        score_label.grid(row=cpt_y, column=cpt_x)
        for j in i.get_Attributs():
            cpt_x+=1
            my_label=tkinter.Label(variants_frame, text=j)
            my_label.grid(row=cpt_y, column=cpt_x)