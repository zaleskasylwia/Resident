class Community:
    def __init__(self, year_of_fundation, address, employees=None, residents=None):
        self.year_of_fundation = year_of_fundation
        self.address = address
        self.employees = employees or []
        self.residents = residents or []