from myclass import Color
class MyBox:
    def __init__( self ):
        self._theItems =list()

    def __len__( self ):
        return len( self._theItems )

    def add( self, item ):
        self._theItems.append( item )

    def remove( self, item ):
        assert item in self._theItems # precondition
        idx = self._theItems.index( item )
        return self._theItems.pop( idx )

    def __contains__( self, item ):
        return item in self._theItems

    def __iter__( self, item ):
        return MyBoxIterator(self._theItems)

color1=Color()
color1.calculate()
color1.changecolor(13,16,25)

color1.calculate()




