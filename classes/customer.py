from os import name

class Customer:
    def __init__(self,name_surname,number,start_date,end_date):
        self.name_surname = name_surname
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
    
    def setNameSurname(self,value):
        self.name_surname = value
    
    def getNameSurname(self):
        return self.name_surname

    def setNumber(self,value):
        self.number = value
    
    def getNumber(self):
        return self.number
    
    def setStartDate(self,value):
        self.start_date = value
    
    def getStartDate(self):
        return self.start_date

    def setEndDate(self,value):
        self.end_date = value
        
    def getEndDate(self):
        return self.end_date

    def getStartEndDateStr(self):
        return self.start_date + "," + self.end_date