from exception_handling import check_if_number


class Menu():
    def menu_main_graphic(self):
        print("")
        print("Huvudmenyn.")
        print("[ 1 ] Sök efter film")
        print("[ 2 ] Visa senaste sökningar")
        print("[ 0 ] Avsluta")

    def menu_sub_graphic(self):
        print("")
        print("Historiks menyn.")
        print("[ 1 ] Visa information om senaste sökta filmer")
        print("[ 2 ] Visa information om vald sökt film")
        print("[ 0 ] Avsluta")

    def menu_search_graphic(self):
        print("Välj film")
        print("Titel - Årtal")
        print("[ 0 ] Avsluta")

    def menu_input_number(self):
        choice = check_if_number()
        return choice
