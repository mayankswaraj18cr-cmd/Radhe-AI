class ProceduralMemory:
    def __init__(self):
        self.procedures = []

    def remember(self, procedure):
        self.procedures.append(procedure)
        return procedure
