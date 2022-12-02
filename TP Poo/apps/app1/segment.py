from point import * 
class Segement():

    def __init__(_self, x2, y2 , x1 = 0 , y1 = 0 ):
        _self.origine = Point(x1,y1)
        _self.exterem = Point(x2,y2)
    
    def __str__(_self):
        return "Segment d'origine ({},{}) et d'extrimité ({},{})".format(_self.origine.x , _self.origine.y , _self.exterem.x , _self.exterem.y )
        