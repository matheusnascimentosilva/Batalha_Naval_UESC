class CrusierModelCrazy (object):

    def __init__(self):
        super.__init__()

        self.ship_name = "Hidroaviao - Feira Malhado"
        self.ship_code = "FEIRA"
        
        # Hidroaviao pra cima
        self.ship_size_up = [2][3] = [["","F",""]
                                      ["F","","F"]]
        #Hidroaviao para a direita
        self.ship_size_dir = [3][2] = [["F",""]
                                       ["","F"]
                                       ["F",""]]
        #Hidroavião para baixo
        self.ship_size_down = [2][3] = [["F","","F"]
                                        ["","F",""]]
        #Hidroavião para esquerda
        self.ship_size_esq = [3][2] = [["","F"]
                                       ["F",""]
                                       ["","F"]]

    # Tentativas de tentar representar essa embarcaç~]ao estranha
    
    # Gets ---------------------------
    @property
    def ship_name( self ):
        return self._ship_name
    
    @property
    def ship_code( self ):
        return self._ship_code
    
    @property
    def ship_size_up( self ):
        return self._ship_size
    
    @property
    def ship_size_dir( self ):
        return self._ship_size
    
    @property
    def ship_size_down( self ):
        return self._ship_size
    
    @property
    def ship_size_esq( self ):
        return self._ship_size