import re

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
    print("comparaison :"+working_value+" "+operator+" "+value)
    if operator == ">" :
        if working_value > value :
            return True
        else :
            return False
    elif operator == ">=" :
        if working_value >= value :
            return True
        else :
            return False

    elif operator == "<" :
        if working_value < value :
            return True
        else :
            return False

    elif operator == "<=":
        if working_value <= value :
            return True
        else :
            return False

    elif operator == "=":
        if working_value == value :
            return True
        else :
            return False

    elif operator == "!=":
        if working_value != value :
            return True
        else :
            return False

    elif operator == "match":
        if re.match(working_value, value) :
            return True
        else :
            return False

    elif operator == "contain":
        if working_value > value:
            return True
        else:
            return False
    elif operator == "don't contain":
        if working_value > value:
            return True
        else:
            return False


