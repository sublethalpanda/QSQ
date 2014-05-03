

class Selection():
    txt = ""
    vSelections = []
    codeToExecute = ""
    def __init__(self, txt, vSelections, codeToExecute):
        self.txt = txt
        self.vSelections = vSelections
        self.codeToExecute = codeToExecute

    def __str__(self):
        return self.txt

    def validSel(self, txt):
        return txt in self.vSelections

    def select(self):
        pass