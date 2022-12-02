from date import *
class Emprunt():

    def __init__(_self , numLivre , ncin_abonne , dateEmp   ) :
        _self.numLivre = numLivre
        _self.ncin_abonne = ncin_abonne
        _self.dateEmp = dateEmp
        _self.dateRetour = dateEmp.jour + 10
        _self.penalite = False
    
    def majPenalite(_self ,actualDate ):
        if _self.dateRetour.jour > actualDate.jour  :
            _self.penalite = True
        