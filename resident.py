from .person import Person


class Resident(Person):
    def __init__(self, first_name, last_name, flat_nr, flat_area, price_per_metr):
        super().__init__(firts_name, last_name)
        self.flat_nr = flat_nr
        self.flat_area = flat_area
        self.price_per_metr = price_per_metr

    def __str__(self):
        return "{} {} {} {} {}".format(self.first_name, self.last_name, self.flat_nr, self.flat_area, self.price_per_metr)

    def calculate_rent(self):
        return int(self.flat_area * self.price_per_metr)