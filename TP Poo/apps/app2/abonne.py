class Abonne():
    __nCIN = []

    def __init__(_self , ncin , nom , est_penaliser , nb_emprunt  ) :
        if(ncin not in Abonne.__nCIN):
            _self.__ncin = ncin
            _self.nom  = nom 
            _self.__est_penaliser = est_penaliser 
            _self.__nb_emprunt = nb_emprunt
            print("Abonné ajouter avec succés ")
        else:
            print("Abonné deja ajouter !  ")
        
    def __str__(_self):
        isPenliser = "n'est pas pénaliser"
        if(_self.__est_penaliser):
            isPenliser = "est pénaliser"

        return'''
          NCIN : {0} 
          Nom : {1}
          Prenom : {2}
          état : {3}
        '''.format(_self.__ncin , _self.nom , _self.prenom ,isPenliser )
    
    def getNcin(_self):
        return _self.__ncin
    
    def getPenaliser(_self):
        return _self.__est_penaliser

    def marquer_retour(_self):
        if(_self.__nb_emprunt > 0):
            _self.__nb_emprunt -=1  
    
    def marquer_emprunt(_self):
            _self.__nb_emprunt +=1  


        