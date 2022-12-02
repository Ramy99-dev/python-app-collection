class Livre():
    __num_livre = 0

    def __init__(_self , t , nb_ex ) :
        _self.num  = Livre.__num_livre
        _self.titre = t
        _self.nbExemplaire = nb_ex
        Livre.__num_livre +=1
    
    def __str__(_self):
        return '''
                Livre numero : {0}
                Titre : {1}
                Nombre exemplaire : {2}
               '''.format(_self.num , _self.titre , _self.nbExemplaire)
    def est_disponible(_self):
        if(_self.nbExemplaire >0):
            return True
        return False
    
    def retirer_un_exemplaire(_self):
        if(_self.nbExemplaire > 0):
            _self.nbExemplaire -=1
        else:
            print("Insuffisant")

    def retour_exemplaire(_self):
        _self.nbExemplaire +=1