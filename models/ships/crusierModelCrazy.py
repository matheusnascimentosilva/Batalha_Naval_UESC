class CrusierModelCrazy (object):

    def __init__(self):
        super.__init__()

        self.ship_name = "Hidroaviao - Feira Malhado"
        self.ship_code = "FEIRA"
        self.ship_size = 6

    
    # Gets ---------------------------
    @property
    def ship_name( self ):
        return self._ship_name
    
    @property
    def ship_code( self ):
        return self._ship_code
    
    @property
    def ship_size( self ):
        return self._ship_size
    