class Variant:
    #Variants are defined by attributs, it's the data we load from a tsv file, and by a score which we calculate.
    def __init__(self, attributs_list=None, score=None, type=None):
        if attributs_list is None:
            self.Attributs = [""]
        else:
            self.Attributs= attributs_list
        if score is None:
            self.Score = [""]
        else:
            self.Score= score
        is type is None:
            self.Type = "UKN"
        else:
            self.Type=type

    #Set the list of attributs
    def set_Attributs(self, attributs_list):
        self.Attributs=attributs_list

    #Set the score
    def set_Score(self, score):
        self.Score=score

    #Set the type
    def set_Type(self, type):
        self.Type=type

    #return the type
    def get_Type(self):
        return self.Type

    #return the score
    def get_Score(self):
        return self.Score

    #Return the list of attributes
    def get_Attributs(self):
        return self.Attributs

    #return only one attributes at the specified index
    def get_one_attribut(self, i):
        return self.Attributs[i]

    #print all info about this instance. Use for debug purposes.
    def describe(self):
        print("L'objet variant contient ces infrmations :")
        print(self.get_Score())
        print(self.get_Attributs())



