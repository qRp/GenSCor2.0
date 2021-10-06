import re
from Rules import *
from Variant import *

def score_it(rule, variant):
    to_return = 0
    for i in range(len(rule.get_column())):
        working_value = variant.get_Attributs()[rule.get_column()[i]]
        result = compare(working_value, rule.operator[i], rule.value[i])
        if result:
            to_return+=1
    if to_return == len(rule.get_column()):
        if rule.get_sens() == "up":
            variant.set_Score(variant.get_Score() + rule.get_score_val())
        elif rule.get_sens() == "down":
            variant.set_Score(variant.get_Score() - rule.get_score_val())
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
    variants_list = []
    f = open(file_path, "r")
    lines = f.readlines()
    for line in lines:
        data_line = line.split()
        variants_list.append(Variant(data_line))
    return variants_list


def export_data(file_path, variants_list):
    f = open(file_path, "w")
    for i in variants_list:
        f.write(str(i.get_Score())+"\t")
        for j in i.get_Attributs():
            f.write(j+"\t")
        f.write("\n")

