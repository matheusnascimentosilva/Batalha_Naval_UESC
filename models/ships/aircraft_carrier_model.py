class AircraftCarrierModel( object ):
    
    def __init__( self ):
        super().__init__()
        
        self._ship_name = "Porta-Aviões - Salobrinho"
        self._ship_code = "SALOBRINHO"
        self._ship_size = 5
    
    # Gets ---------------------------------
    @property
    def ship_name( self ):
        return self._ship_name
    
    @property
    def ship_code( self ):
        return self._ship_code
    
    @property
    def ship_size( self ):
        return self._ship_size
    