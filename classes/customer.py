##
## Created: 24.01.2021, Ali Babayev
##

class Customer:
    def __init__(self,name_surname,number,start_date,end_date):
        self._name_surname = name_surname
        self._number = number
        self._start_date = start_date
        self._end_date = end_date
    
    @property    
    def name_surname(self):
        return self._name_surname

    @name_surname.setter
    def name_surname(self,value):
        self._name_surname = value
    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self,value):
        self._number = value
  
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self,value):
        self._start_date = value
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self,value):
        self._end_date = value
      
    def get_start_end_date_list(self):
        return [int(self._start_date), int(self._end_date)]
