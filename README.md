# Resident

## klasa Resident:

Imię

Nazwisko

nr mieszkania

metraż mieszkania

stawka za m2

### metody:

-__init__

- __str__ zwracająca stringa z pełnymi danymi mieszkańca

-calculate_rent - zwraca integera wysokość czynszu

obsługa budynku:

## klasa Employee:

Imię

Nazwisko

funkcja

rok zatrudnienia

stawka godzinowa

### metody:

-__init__

- __str__ zwracająca stringa z pełnymi danymi pracownika

- calculate_salary zwraca integera wysokość pensji (przyjmuje jako argument ilość przepracowanych godzin w danym miesiącu)

## klasa Community:

Nazwa spółdzielni

rok założenia

adres

lista pracowników

lista mieszkańców

### metody:

-__init__

-add_employee

-add_resident

-save_community_to_file

-read_community_from_file

-find_longest_working_employee

-calculate_total_community_area
