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

    def save_community_to_file(self):
        pass

    def read_community_from_file(self):
        pass

    def find_longest_working_employee(self):
        pass

    def calculate_total_community_area(self):
        pass