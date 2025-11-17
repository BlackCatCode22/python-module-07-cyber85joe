# Main.py
# driver file for zoo keeper's challenge

from datetime import date

from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Bear import Bear
from Tiger import Tiger

# create lists of the species
list_of_hyenas = []
list_of_lions = []
list_of_bears = []
list_of_tigers = []

# today's date
current_date = date.today()
current_year = current_date.year


def calc_birth_date(the_season, the_years):
    year_of_birth = int(current_year) - int(the_years)

    the_season = the_season.lower()

    if "spring" in the_season:
        return f"{year_of_birth}-03-21"
    elif "summer" in the_season:
        return f"{year_of_birth}-06-21"
    elif "fall" in the_season:
        return f"{year_of_birth}-09-21"
    elif "winter" in the_season:
        return f"{year_of_birth}-12-21"
    else:
        return f"{year_of_birth}-01-01"


def process_one_line(one_line):

    print(one_line)

    words = one_line.strip().split(",")
    print(words)

    # parse fields
    part1 = words[0].strip().split(" ")

    age_in_years = part1[0]
    a_sex = part1[3]
    a_species = part1[1].lower()

    part2 = words[1].strip().split(" ")
    season = part2[2]

    color = words[2].strip()
    weight = words[3].strip()
    origin_01 = words[4].strip()
    origin_02 = words[5].strip()

    from_zoo = origin_01 + "," + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    # create objects depending on species
    if "hyena" in a_species:
        my_hyena = Hyena("aName","anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_ID = "Hy" + str(Hyena.numofHyenas).zfill(2)
        list_of_hyenas.append(my_hyena)

    elif "lion" in a_species:
        my_lion = Lion("aName","anID" , birth_day, color, a_sex, weight, from_zoo, current_date)
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_ID = "Li" + str(Lion.numoflions).zfill(2)
        list_of_lions.append(my_lion)

    elif "tiger" in a_species:
        my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        my_tiger.animal_ID = "Ti" + str(Tiger.numofTigers).zfill(2)
        list_of_tigers.append(my_tiger)

    elif "bear" in a_species:
        my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_ID = "Be" + str(Bear.numofBears).zfill(2)
        list_of_bears.append(my_bear)


# open file
file_path = r'C:\Users\0889748\Desktop\py4e\zoo_keeper\arrivingAnimals.txt'

with open(file_path, "r") as file:
    for line in file:
        process_one_line(line)

# output counts
print(f"\nNumber of animals created: {Animal.numofAnimals}")
print(f"Number of hyenas created: {Hyena.numofHyenas}")
print(f"Number of lions created: {Lion.numoflions}")
print(f"Number of tigers created: {Tiger.numofTigers}")
print(f"Number of bears created: {Bear.numofBears}")

# output animals
print("\nZookeeper's Challenge Population\n")

print("Hyena Habitat:")
for h in list_of_hyenas:
    print(f"{h.animal_ID}, {h.name}; birthdate: {h.birth_date}; {h.color}; {h.sex}; {h.weight}; {h.originating_zoo}; arrived: {h.date_arrival}")

print("\nLion Habitat:")
for l in list_of_lions:
    print(f"{l.animal_ID}, {l.name}; birthdate: {l.birth_date}; {l.color}; {l.sex}; {l.weight}; {l.originating_zoo}; arrived: {l.date_arrival}")

print("\nBear Habitat:")
for b in list_of_bears:
    print(f"{b.animal_ID}, {b.name}; birthdate: {b.birth_date}; {b.color}; {b.sex}; {b.weight}; {b.originating_zoo}; arrived: {b.date_arrival}")

print("\nTiger Habitat:")
for t in list_of_tigers:
    print(f"{t.animal_ID}, {t.name}; birthdate: {t.birth_date}; {t.color}; {t.sex}; {t.weight}; {t.originating_zoo}; arrived: {t.date_arrival}")


