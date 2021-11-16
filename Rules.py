class Rules:
    def __init__(self,status="on",column=[0], operator=["="], value=[0], sens="up", score_val=0):
        #status may be on or off : active or inactive
        self.status=status
        #a list of index of variants.attributs
        self.column=column
        #a list of operator
        self.operator=operator
        #a list of value to compare variant.attriuts[index] to
        self.value=value
        #may be up or down : the effect on the score
        self.sens=sens
        # the value to add or substract to the score
        self.score_val=score_val

    #return the status of the rules
    def get_status(self):
        return self.status

    #return the list of columns
    def get_column(self):
        return self.column

    #return only one column at the specified index.
    def get_one_column(self,i):
        return self.column[i]

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


    #change only one value at the specified index. Used for the GUI.
    def set_one_value(self,value,i):
        # simple case : we are changing one value
        try:
            self.value[i]=value
        # other case : we are adding a new condition
        except IndexError:
            self.value.append(value)

    #change only one column at the specified index. Used for the GUI.
    def remove_one_column(self,i):
        self.column.pop(i)

    #change only one operator at the specified index. Used for the GUI.
    def remove_one_operator(self,i):
        self.operator.pop(i)

    #change only one value at the specified index. Used for the GUI.
    def remove_one_value(self,i):
        self.value.pop(i)

    #print everything about the rule. Used for debug purposes.
    def describe(self):
        print("L'instance de l'objet Rule est composé de :")
        print(self.get_status())
        print(self.get_column())
        print(self.get_operator())
        print(self.get_value())
        print(self.get_sens())
        print(self.get_score_val())

    #convert the rule to a json string for saving.
    def convert_to_json(self):
        size_list=len(self.get_column())
        my_json='{"Status": "'+self.get_status()+'","Column": ['
        cpt=0
        for i in self.get_column():
            cpt+=1
            my_json=my_json+'"'+str(i)+'"'
            if cpt < size_list:
                my_json=my_json+','
            else :
                my_json=my_json+'], "Operator": ['
        cpt=0
        for i in self.get_operator():
            cpt+=1
            my_json=my_json+'"'+str(i)+'"'
            if cpt < size_list:
                my_json=my_json+','
            else :
                my_json=my_json+'], "Value": ['
        cpt=0
        for i in self.get_value():
            cpt+=1
            my_json=my_json+'"'+str(i)+'"'
            if cpt < size_list:
                my_json=my_json+','
            else :
                my_json=my_json+'], "Sens":"'
        my_json = my_json+self.get_sens()+'","Score_val": "'+str(self.get_score_val())+'"}'
        return my_json
