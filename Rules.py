class Rules:
    def __init__(self,status="on",column=[], operator=[], value=[], sens="up", score_val=0):
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

    def get_status(self):
        return self.status

    def get_column(self):
        return self.column

    def get_sens(self):
        return self.sens

    def get_score_val(self):
        return self.score_val

    def set_status(self,status):
        self.status=status

    def set_sens(self,sens):
        self.sens=sens

    def set_score_val(self,score_val):
        self.score_val=score_val

    def get_operator(self):
        return self.operator

    def get_value(self):
        return self.value

    def set_column(self,column):
        self.column=column

    def set_operator(self,operator):
        self.operator=operator

    def set_value(self,value):
        self.value=value

    def describe(self):
        print("L'instance de l'objet Rule est composé de :")
        print(self.get_status())
        print(self.get_column())
        print(self.get_operator())
        print(self.get_value())
        print(self.get_sens())
        print(self.get_score_val())

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
