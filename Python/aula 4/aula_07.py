class Televisão:
    def __init__ (self):
        self.ligada= False
    def power (self):
        if self.ligada:
            self.ligada= False
        else:
            self.ligada= True

televisão= Televisão()
print(televisão.ligada)
televisão.power()
print(televisão.ligada)
televisão.power()
print(televisão.ligada)
