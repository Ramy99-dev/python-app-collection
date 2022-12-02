class Date(): 
    def __init__(_self , jour , mois , annee ) :
        _self.jour = jour 
        _self.mois = mois 
        _self.annee = annee
    def __str__(_self) :
        return "La date : {0}/{1}/{2}".format(_self.jour , _self.mois , _self.annee)