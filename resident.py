from .person import Person


class Resident(Person):
    def __init__(self, first_name, last_name, flat_nr, flat_area, price_per_metr):
        super().__init__(firts_name, last_name)
        self.flat_nr = flat_nr
        self.flat_area = flat_area
        self.price_per_metr = price_per_metr