class Variant:
    def __init__(self, attributs_list=[], score=0):
        self.Attributs=attributs_list
        self.Score=score

    def set_Attributs(self, attributs_list):
        self.Attributs=attributs_list

    def set_Score(self, score):
        self.Score=score

    def get_Score(self):
        return self.Score

    def get_Attributs(self):
        return self.Attributs

    def describe(self):
        print("L'objet variant contient ces infrmations :")
        print(self.get_Score())
        print(self.get_Attributs())