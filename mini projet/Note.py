class Note:
    def __init__(self, numEtu, codeCours, note):
        self._numEtudiant = numEtu
        self._codeCours =codeCours
        self._note = note
    
    def _getNumEtudiant(self):
        return self._numEtudiant
    def _setNumEtudiant(self, num):
        self._numEtudiant = num
    numEtudiant = property(_getNumEtudiant, _setNumEtudiant)

    def _getCodeCours(self):
        return self._codeCours
    def _setCodeCours(self, code):
        self._codeCours = code
    codeCours = property(_getCodeCours, _setCodeCours)

    def _getNote(self):
        return self._note
    def _setNote(self, note):
        self._note = note
    note = property(_getNote, _setNote)
