from movies import Movies
from menu import Menu
import movies
from json_handling import Json


movies = Movies()
menu = Menu()
json = Json()


def menu_main():
    print("")
    print("Välkommen till MovieFinder")
    menu.menu_main_graphic()
    choice_menu = menu.menu_input_number()

    while choice_menu != 0:
        if choice_menu == 1:
            print()
            movies.search_movie()
        elif choice_menu == 2:
            print()
            menu_history()
        else:
            print()
            print("Skriv endast in giltiga nummer.")
        print("")
        menu.menu_main_graphic()
        choice_menu = menu.menu_input_number()

    json.save_to_json()


def menu_history():
    print("")
    menu.menu_sub_graphic()
    choice_menu_history = menu.menu_input_number()

    while choice_menu_history != 0:
        if choice_menu_history == 1:
            print("")
            movies.print_history()
        elif choice_menu_history == 2:
            print("")
            movies.show_information()
        else:
            print("Skriv endast in giltiga nummer.")

        menu.menu_sub_graphic()
        choice_menu_history = menu.menu_input_number()


json.read_from_json()


menu_main()
