class Rectangle():

 def __init__(_self , largeur , longeur):
    _self.nom     = "rectangle"
    _self.longeur = longeur
    _self.largeur = largeur

 
 def __str__(_self):
    return  "Triangle de longeur  = {0} et de largeur = {1} ".format(_self.longeur , _self.largeur )
 def calculeSurface(_self):
    return (_self.longeur * _self.largeur) / 2



