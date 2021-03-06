from person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, position, year_of_emp, rate_per_hour):
        super().__init__(first_name, last_name)
        self.position = position
        self.year_of_emp = year_of_emp
        self.rate_per_hour = rate_per_hour

    def __str__(self):
        return "{} {} {} {} {}".format(self.first_name, self.last_name, self.position, self.year_of_emp, self.rate_per_hour)

    def caluclate_salary(self, working_hours):
        if type(working_hours) is int or type(working_hours) is float:
            return int(self.rate_per_hour * working_hours)
        else:
            raise TypeError

    def __lt__(self, other):
        return self.year_of_emp < other.year_of_emp
