from livre import *
from emprunt import *
class Bibiotheque():
    def __init__(_self) :
        _self.livres = {}
        _self.emprunteurs = {}
        _self.operations = {}

    def ajouter_livre(_self , l ):
        if(l.num in _self.livres):
            print("Ce livre est déja inseré")
        else:
            _self.livres[l.num] = l

    def ajouter_abonne(_self , a):
         if(a.getNcin() in _self.emprunteurs):
            print("L'abonné est déja inseré")
         else:
            _self.emprunteurs[a.getNcin()] = a
    
    def __str__(_self):
        return '''
           Livres = {0}
           Emprunteurs = {1}
           Operations = {2}
        '''.format(_self.livres , _self.emprunteurs , _self.operations)
    
    def livre_empruntes(_self , ncin  ):
        livres = []
        for i in _self.operations.keys():
            if(i[0] == ncin):
                livres.append(i[1])
        
        return livres 
    
    def ont_empruntes(_self , num_liv ):
        abonnes = []
        for i in _self.operations.keys:
            if(i[1] == num_liv):
                abonnes.append(i[1])
        
        return abonnes 
    
    def emprunter(_self , ncin , num_livre ):
        if(ncin not in _self.emprunteurs):
            print("L'abonnée n'est pas inserer ")
        else:
            abonne = _self.emprunteurs[ncin]
            if(abonne.getPenaliser()):
                print("Désole , l'abonné est pénaliser ")
            else:
                res = _self.livre_empruntes(ncin)
                if(num_livre in res ):
                    print("Le livre est déja emprunter ! par l'abonné {0} " .format(_self.ncin))
                else:
                    if(num_livre not in _self.livres):
                        print("Hors stock ")
                    else:
                        _self.operations[(ncin , num_livre)] = Emprunt(num_livre , ncin , Date(2,12,2022))
                        _self.livres[num_livre].retirer_un_exemplaire()
                        _self.emprunteurs[ncin].marquer_emprunt()
        

        