from abonne import *
class Abonne_restreint(Abonne):
    def __init__(_self , ncin , nom , est_penaliser , nb_emprunt , max_emprunt ) :
        super().__init__(ncin , nom , est_penaliser , nb_emprunt)
        _self.max_emprunt = max_emprunt
        
    def __str__(_self):
        isPenliser = "n'est pas pénaliser"
        if(_self.__est_penaliser):
            isPenliser = "est pénaliser"

        return'''
          NCIN : {0} 
          Nom : {1}
          Prenom : {2}
          état : {3}
          max Emprunt : {4}
        '''.format(_self.__ncin , _self.nom , _self.prenom ,isPenliser , _self.max_emprunt )
    
   
   
    
    def marquer_emprunt(_self):
        if(_self.__nb_emprunt < _self.max_emprunt):
            _self.__nb_emprunt +=1  
        else:
            print("Désole vous avez atteind le nombre max d'emprunt .")

