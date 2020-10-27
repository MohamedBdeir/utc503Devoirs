class Cours:
    """Classe définissant un cours caractérisé par un code, un intitulé et  un niveau"""

    def __init__(self, code, intitule, niveau):
        self._code = code
        self._intitule = intitule
        self._niveau = niveau
    
    def _getCode(self):
        return self._code
    def _setCode(self, code):
        print("Impossible de modifier le code d'un cours")

    code = property(_getCode, _setCode)

    def _getIntitule(self):
        return self._intitule
    def _setIntitule(self, _intitule):
        self._intitule = _intitule
    intitule = property(_getIntitule, _setIntitule)

    def _getNiveau(self):
        return self._niveau
    def _setNiveau(self, niveau):
        self._niveau = niveau
    niveau = property(_getNiveau, _setNiveau)    