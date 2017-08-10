import csv


class Community:

    def __init__(self, community_name, year_of_fundation, address):
        if type(community_name) is str and type(year_of_fundation) is int and type(address) is str:
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
        HEADERS = ['Community name', 'Year of fundation', 'address']
        with open('{}.csv'.format(self.community_name), 'w', newline='') as csvfile:
            community_writer = csv.writer(csvfile)
            community_writer.writerow(HEADERS)
            community_writer.writerow([self.community_name, self.year_of_fundation, self.address])

    def read_community_from_file(self, csv_path):
        community = []
        with open(csv_path) as csvfile:
            community_reader = csv.reader(csvfile)
            next(community_reader)  # skip heades
            for data in community_reader:
                community.append(data)
        return community

    def find_longest_working_employee(self):
        pass

    def calculate_total_community_area(self):
        total_community_area = 0
        for flat_area in self.resident:
            total_community_area += flat_area

        return total_community_area


def main():
    com = Community("Nauczyciela", 2014, "Szkolan 41 Oświęcim")
    com.save_community_to_file()
    ab = Community("Na", 2014, "Kraków")
    ab.save_community_to_file()
    print(com.read_community_from_file("Nauczyciela.csv"))
    print(ab.read_community_from_file("Na.csv"))

if __name__ == "__main__":
    main()