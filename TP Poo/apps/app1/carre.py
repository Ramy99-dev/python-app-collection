from rectangle import * 
class Carre(Rectangle):
    def __init__(_self , largeur , longeur):
        super().__init__(largeur , longeur)
        _self.nom  = "carre"
    def calculeSurface(_self):
        return (_self.longeur * _self.largeur) 




