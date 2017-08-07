from .person import Person

class Employee(Person):
    def __init__(self, first_name, last_name, position, year_of_emp, rate_per_hour):
        super().__init__(first_name, last_name)
        self.position = position
        self.year_of_emp = year_of_empk
        self.rate_per_hour = rate_per_hour