from Glob import *
class Rules:
    def __init__(self,status=None, operator=None, value=None, sens=None, score_val=None, text_column=None,column=None):
        #the structure with the none keyword is to avoid sharing a list between all instances of the classe
        #It's a weird python way of doing things I guess.
        # status may be on or off : active or inactive
        if status is None: #status may be on or off : active or inactive
            self.status = "on"
        else:
            self.status = status
        if column is None: #a list of indexes of variants.attributs
            self.column = [0]
        else:
            self.column = list(column)
        if operator is None:#a list of operator
            self.operator = ["="]
        else:
            self.operator = list(operator)
        if value is None:#a list of value to compare variant.attriuts[index] to
            self.value = [0]
        else:
            self.value = list(value)
        if sens is None:#may be up or down : the effect on the score
            self.sens = "up"
        else:
            self.sens = sens
        if score_val is None:# the value to add or substract to the score
            self.score_val = 0
        else:
            self.score_val = score_val
        if text_column is None:#the header of the selected columns
            self.text_column = [""]
        else:
            self.text_column = list(text_column)


    #return the status of the rules
    def get_status(self):
        return self.status

    #return the list of columns
    def get_column(self):
        return self.column

    #return the list of textcolumns
    def get_text_column(self):
        return self.text_column

    #return only one column at the specified index.
    def get_one_column(self,i):
        return self.column[i]

    #return only one column at the specified index.
    def get_one_text_column(self,i):
        return self.text_column[i]

    #return only one operator at the specified index
    def get_one_operator(self, i):
        return self.operator[i]

    #return only one value at the specified index
    def get_one_value(self, i):
        return self.value[i]

    #return the direction of the score change
    def get_sens(self):
        return self.sens

    #return the score value to add or substract
    def get_score_val(self):
        return self.score_val

    #change the status of the rule
    def set_status(self,status):
        self.status=status

    #change the direction of the score
    def set_sens(self,sens):
        self.sens=sens

    #change the score value to add or substract
    def set_score_val(self,score_val):
        self.score_val=score_val

    #return the list of operators
    def get_operator(self):
        return self.operator

    #return the list of values
    def get_value(self):
        return self.value

    #change the list of columns.
    def set_column(self,column):
        self.column=column

    #change the list of operators
    def set_operator(self,operator):
        self.operator=operator

    #change the list of values
    def set_value(self,value):
        self.value=value

    #change only one column at the specified index. Used for the GUI.
    def set_one_column(self,column,i):
        #simple case : we are changing one value
        try:
            self.column[i]=column
        #other case : we are adding a new condition
        except IndexError:
            self.column.append(column)

    #change only one operator at the specified index. Used for the GUI.
    def set_one_operator(self,operator,i):
        # simple case : we are changing one value
        try:
            self.operator[i]=operator
        # other case : we are adding a new condition
        except IndexError:
            self.operator.append(operator)

    def set_one_text_column(self,text_column,i):
        #simple case : we are changing one value
        try:
            self.text_column[i]=text_column
        #other case : we are adding a new condition
        except IndexError:
            self.text_column.append(text_column)


    #change only one value at the specified index. Used for the GUI.
    def set_one_value(self,value,i):
        print(L["set one value"][lang] + str(value) + str(i))
        self.describe()
        # simple case : we are changing one value
        try:
            self.value[i]=value
        # other case : we are adding a new condition
        except IndexError:
            self.value.append(value)

    #change only one column at the specified index. Used for the GUI.
    def remove_one_column(self,i):
        self.column.pop(i)

    #change only one textcolumn at the specified index. Used for the GUI.
    def remove_one_text_column(self,i):
        self.text_column.pop(i)

    #change only one operator at the specified index. Used for the GUI.
    def remove_one_operator(self,i):
        self.operator.pop(i)

    #change only one value at the specified index. Used for the GUI.
    def remove_one_value(self,i):
        self.value.pop(i)

    #print everything about the rule. Used for debug purposes.
    def describe(self):
        print("The instance of the 'Rule' object "+str(self)+" contains :")
        print(self.get_status() +"  "+ self.get_sens() +"  "+ str(self.get_score_val()))
        print(self.get_column() + self.get_text_column() + self.get_operator() + self.get_value())


