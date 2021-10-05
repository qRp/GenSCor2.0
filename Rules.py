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

