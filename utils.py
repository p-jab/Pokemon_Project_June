'''Task 0: Import the modules csv and random'''
import csv, random

def startup():
    print("\t"*5, "Pokemon Trainer APP")

def options():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Check your Pokemon', 'Add a new Pokemon', 'Show all Pokemon', 'Visualise' ,'Save your Pokedex' and 'Exit'

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    print("Choose an item from the menu:\n1-Check your Pokemon\n2-Add a new Pokemon\n3-Show all Pokemon\n4-Visualise\n5-Save your Pokedex\n0-Exit")
    opt  = int(input("Your option: "))
    if opt in [1,2,3,4,5,0]:
        return opt

def check_poke():
    """
    Task 3: Display a menu of options for how a Pokemon should be searched. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By name', 'By type'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("How would you like to search?:\n1-By Name\n2-By Type")
    opt  = int(input("Your option: "))
    if opt in [1,2]:
        return opt

def add_poke():
    """
    Task 4: Display a menu of options for how a Pokemon should be added. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Add specific', 'Add at random'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("How would you like to add a Pokemon?:\n1-Add Specific\n2-Add at Random")
    opt  = int(input("Your option: "))
    if opt in [1,2]:
        return opt

def visualise():
    """
    Task 5: Display a menu of options for how a graph should be produced. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By Generation (Pie Chart)', 'By Type (Bar Chart)'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("How would you like to visualise your Pokemon?\n1-By Generation (Pie Chart)\n2-By Type (Bar Chart")
    opt  = int(input("Your option: "))
    if opt in [1,2]:
        return opt


def by_name(p_list = []):
    
    """
    Task 6: Display a pokemon from the list, searching by name.

    The p_list is a list of pokemon.
    Prompt the user to enter name of the pokemon they are searching for.
    The function should display all the details related only to that single pokemon, if it's on the p_list.
    If pokemon of such name does not exist on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    p_name = input("Enter name of a Pokemon: ") #squirtle
    for pokemon in p_list: # pikach, ekans, koffin
        if pokemon[1].upper() == p_name.upper():
           print(pokemon)
           return
    print("Pokemon not on the list!")

def by_type(p_list = []):
    
    """
    Task 7: Display pokemon from the list, searching by type.

    The p_list is a list of pokemon.
    Prompt the user to enter type of the pokemon they are searching for.
    The function should display all the details related only to pokemon of that type,
    if it's on the p_list.
    If no such pokemon of that type exists on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    p_type = input("Enter type of a Pokemon: ")
    for pokemon in p_list:
        if pokemon[2].upper() == p_type.upper() or pokemon[3].upper() == p_type.upper():
           print(pokemon)
           return
    print("Pokemon not on the list!")

def add_specific_poke():
    
    """
    Task 8: Search for pokemon in the database, and return it if it's found.

    Access pokemon_database.csv using appropriate module.
    Search through this database, looking for a pokemon by it's name.
    If no such pokemon exists, then display appropriate message and return None.

    :param: None
    :return: A list representing a pokemon or None
    """
    with open("pokemon_database.csv") as dtb:
        reader = csv.reader(dtb)
        p_name = input("Enter name of a Pokemon: ")
        for pokemon in reader:
            if pokemon[1].lower() == p_name.lower():
                return pokemon
        print("Pokemon does not exist!")

def add_random_poke():
    
    """
    Task 9: Search for a random pokemon in the database, and return it.

    Access pokemon_database.csv using appropriate module.
    Pick out a random pokemon and return it.

    :param:  None
    :return: A list representing a pokemon
    """
    with open("pokemon_database.csv") as dtb:
        reader = csv.reader(dtb)
        number = random.randint(1, 802)
        poke_list = []
        for pokemon in reader:
            poke_list.append(pokemon)
        return poke_list[number]

def show_all(pokedex = []):
    """
    Task 10: Print all pokemon from pokedex.

    Print key information about all the pokemon in the pokedex. Include their
    name, type, total, hp and generation.

    :param p_list: None
    :return: None
    """
    for pokemon in pokedex:
        print(f"Name: {pokemon[1]}\tType: {pokemon[2]} {pokemon[3]}\t Total: {pokemon[4]}\tHP: {pokemon[5]}\tGeneration: {pokemon[11]}\n")

def save_pokes(pokedex = []):
    """
    Task 11: Save content of the pokedex to a suitable file format
    Print "Saving complete" at the end.

    :param p_list: pokedex: a list of pokemon
    :return: None
    """
    with open("pokedex.csv", "w", newline="") as pdex:
        writer = csv.writer(pdex)
        for pokemon in pokedex:
            writer.writerow(pokemon)
    print("Saving complete!")

def load_pokes(path):
    """
    Task 11.5: Load up pokemon from a CSV file into a list structure
    :param path: A relative file path to CSV file in string format
    :return: A list of pokemon
    """
    p_list = []
    try:
        with open(path) as f:
            reader = csv.reader(f)
            for pokemon in reader:
                p_list.append(pokemon)
    except FileNotFoundError:
        print("Ooopsie. No such file exist")
    return p_list