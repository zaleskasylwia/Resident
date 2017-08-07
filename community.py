class Community:
    def __init__(self, year_of_fundation, address, employees=None, residents=None):
        self.year_of_fundation = year_of_fundation
        self.address = address
        self.employees = employees or []
        self.residents = residents or []

    def add_employee(self, employee):
        #czy tu mam dodawać przez klase Employee?
        if employee not in self.employees:
            self.employees.append(employee)

    def add_resident(self, resident):
        if resident not in self.residents:
            self.residents.append(resident)

    