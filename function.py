import re
import tkinter
import tkinter.ttk
import tkinter.filedialog
from Rules import *
from Variant import *
from Glob import *
import json

def score_all():
    global rules_list, variants_list
    for i in variants_list:
        i.set_Score(0)
    for i in rules_list:
        if i.get_status() == "on":
             for j in variants_list:
                score_it(i,j)


def score_it(rule, variant):
    to_return = 0
    rule.describe()
    variant.describe()
    for i in range(len(rule.get_column())):
        working_value = variant.get_Attributs()[int(rule.get_column()[i])]
        result = compare(working_value, rule.operator[i], rule.value[i])
        if result:
            to_return+=1
    if to_return == len(rule.get_column()):
        if rule.get_sens() == "up":
            variant.set_Score(variant.get_Score() + float(rule.get_score_val()))
        elif rule.get_sens() == "down":
            variant.set_Score(variant.get_Score() - float(rule.get_score_val()))
    else:
        return False

#fonction qui renvoie vrai si l'égalité "working_value operator value" est vraie
def compare(working_value, operator, value):
    #Verification de la cohérence des types de données
#    if not float(operator) and not float(value):
#        if operator in ("=", ">", ">=", "<", "<="):
#            print("erreur de type, les opérations =, <, <=, >, >= ne peuvent être appliqués que sur des données numériques")
    print("comparaison :"+str(working_value)+" "+str(operator)+" "+str(value))
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


def load_data(file_path):
    global variants_list, header_list
    variants_list=[]
    f = open(file_path, "r")
    lines = f.readlines()
    header=True
    for line in lines:
        data_line = line.split()
        if header == True:
            header_list=data_line
            header=False
        else :
            variants_list.append(Variant(data_line))


def export_data(file_path):
    global variants_list
    f = open(file_path, "w")
    for i in variants_list:
        f.write(str(i.get_Score())+"\t")
        for j in i.get_Attributs():
            f.write(j+"\t")
        f.write("\n")

def write_rules(file_path):
    global rules_list
    f = open(file_path, "w")
    f.write('{"rules":\n')
    for i in rules_list:
        rule_json=i.convert_to_json()
        f.write(rule_json+"\n")
    f.write('}')

def load_rules(file_path):
    global rules_list
    rules_list=[]
    f = open(file_path, "r")
    lines=f.readlines()
    for line in lines:
        try :
            jdict=json.loads(line)
            rule=Rules(jdict["Status"],jdict["Column"],jdict["Operator"],jdict["Value"],jdict["Sens"], jdict["Score_val"])
            rules_list.append(rule)
        except :
            pass



def preload_rules():
    file=tkinter.filedialog.askopenfilename(filetypes =[('Json Files', '*.json'),('All Files', '*')])
    if file is not None:
        load_rules(file)
    else :
        return 1

def preload_data():
    file=tkinter.filedialog.askopenfilename(filetypes=[('txt Files', '*.txt'),('tsv Files', '*.tsv'),('All Files', '*')])
    if file is not None:
        load_data(file)
    else:
        return 1


def prewrite_rules():
    file=tkinter.filedialog.asksaveasfilename(filetypes=[('json Files', '*.json'),('All Files', '*')], defaultextension=".json")
    if file is not None:
        write_rules(file)
    else:
        return 1

def preexport_data():
    file=tkinter.filedialog.asksaveasfilename(filetypes=[('tsv Files', '*.tsv'),('txt Files', '*.txt'),('All Files', '*')],defaultextension=".tsv")
    if file is not None:
        export_data(file)
    else:
        return 1


def print_all():
    global variants_list, rules_list
    print("Describe all :")
    for i in variants_list:
        i.describe()
    for i in rules_list:
        i.describe()

def list_possible_values(index):
    list_of_values={}
    return_list=[]
    for i in variants_list:
        list_of_values[i.get_one_attribut(index)]=1
    for i in list_of_values.keys():
        return_list.append(i)
    return return_list

def print_GUI_rules():
    global rules_list,GUI_var_list
    #initialisation de la liste de dictionnaire ou sont stockés les boutons
    GUI_var_list = [dict() for x in range(len(rules_list))]
    cpt=0
    index=0
    for i in rules_list:
        cpt=print_rule(i,index,cpt)
        cpt+=1
        index+=1


def print_rule(i,index,cpt):
    global GUI_var_list
    font_on="-overstrike 0"
    font_off="-overstrike 1"
    bg_on="#CEE5D0"
    bg_off="grey"
    def updated_status(i,index):
        i.set_status(GUI_var_list[index]["status"].get())
        if i.get_status() == "on":
            text_label1['font']=font_on
            text_label1['bg']=bg_on
            status_checkbox.select()
        else:
            text_label1['font'] = font_off
            text_label1['bg'] = bg_off

    def updated_sens(i,index):
        print("Update sens")
        #print(GUI_var_list)
        #print(GUI_var_list[index])
        #print(GUI_var_list[index]["sens"].get())
        #i.set_sens(GUI_var_list[index]["sens"].get())
        #here recalcule score

    def updated_score_val(i, index):
        print("Update score val")
        #print(GUI_var_list)
        #print(GUI_var_list[index]["score_value"].get())
        #here recalcule score

    #creation de la checkbox status
    checkbox_var = tkinter.StringVar()
    GUI_var_list[index]["status"]=checkbox_var
    status_checkbox = tkinter.Checkbutton(main_window, variable=GUI_var_list[index]["status"], onvalue="on",
                offvalue="off", command=lambda index=index, i=i: updated_status(i,index))
    if i.get_status() == "on":
        font = font_on
        color = bg_on
        status_checkbox.select()
    else:
        font = font_off
        color = bg_off
    status_checkbox.grid(column=1, row=cpt)

    #Creation du premier label
    text_label1 = tkinter.Label(main_window, text="Si toutes ces conditions sont vrais, le score va")
    text_label1.configure(font=font, bg=color)
    text_label1.grid(column=2, row=cpt)

    #Creation de l'option menu sens
    option_sens = ["up", "down"]
    option_sens_var=tkinter.StringVar()
    GUI_var_list[index]["sens"] = option_sens_var
    GUI_var_list[index]["sens"].set(i.get_sens())
    sens_optionmenu = tkinter.OptionMenu(main_window, option_sens_var, *option_sens,
                                    command=lambda new_value, index=index, i=i: updated_sens(i,index))
    sens_optionmenu.configure(font=font, bg=color)
    sens_optionmenu.grid(column=3, row=cpt)

    #Creation du deuxième label
    text_label2 = tkinter.Label(main_window, text=" de ")
    text_label2.grid(column=4, row=cpt)
    #creation du champs score value
    score_value_var = tkinter.StringVar()
    GUI_var_list[index]["score_value"]=score_value_var
    GUI_var_list[index]["score_value"].set(i.get_score_val())
    GUI_var_list[index]["score_value"].trace_add('write', lambda value, index=index, i=i: updated_score_val(i,index))
    score_value_entry = tkinter.Entry(main_window, textvariable=score_value_var)
    score_value_entry.grid(column=5, row=cpt)

    #creation du troisieme label
    text_label3 = tkinter.Label(main_window, text=" point(s).")
    text_label3.grid(column=6, row=cpt)
    #retour à la ligne et boucle sur les conditions
    for j in range(len(i.get_column())):
        cpt += 1
        #affichage des combobox colonnes
        column_var = tkinter.StringVar()
        GUI_var_list[index]["column"] = column_var
        column_value=int(i.get_one_column(j))
        column_combobox = tkinter.ttk.Combobox(main_window, text=i.get_column()[j])
        column_combobox['values'] = list_possible_values(column_value)
        column_combobox.grid(column=2, row=cpt)
        operator_label = tkinter.Label(main_window, text=i.get_operator()[j])
        operator_label.grid(column=3, row=cpt)
        score_val_label = tkinter.Label(main_window, text=i.get_value()[j])
        score_val_label.grid(column=4, row=cpt)
    return cpt