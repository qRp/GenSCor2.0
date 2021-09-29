class Variant:
    def __init__(self, attributs_list=[], score=2):
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