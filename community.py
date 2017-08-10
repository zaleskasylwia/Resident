class Community:

    def __init__(self, community_name, year_of_fundation, address):
        if type(community_name) is str and type(year_of_fundation) is int and
           type(address) is str and type(employees is list and type(residents) is list:
            self.community_name=community_name
            self.year_of_fundation=year_of_fundation
            self.address=address
            self.employees=[]
            self.residents=[]
        else:
            raise TypeError

    def add_employee(self, employee):
        # czy tu mam dodawać przez klase Employee?
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
        total_community_area = 0
        for flat_area in self.resident:
            total_community_area += flat_area

        return total_community_area

