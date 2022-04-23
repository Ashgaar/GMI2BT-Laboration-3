from exception_handling import check_if_list_error
from menu import Menu
import requests
import json


api_key = "aad791f4"
show_list = []
history_list = []
data_list = []
menu = Menu()


class Movies():
    def search_movie(self):
        if len(show_list) > 0:
            show_list.clear()
        if len(data_list) > 0:
            data_list.clear()
        url = "https://www.omdbapi.com/?apikey=" + api_key + "&s="
        search_title = input("Skriv här vilken film du vill söka på: ")
        history_list.append(search_title)
        resp = requests.get(url + search_title)
        print(resp)
        data = json.loads(resp.text)
        print(data)
        while check_if_list_error(data):
            for entry in data['Search']:
                data_list.append(entry)
            print("")
            if len(data_list) > 1:
                menu.menu_search_graphic()
                i = 1
                for entry in data_list:
                    print("[", i, "]", entry['Title'], entry['Year'])
                    i += 1
                while True:
                    try:
                        show_input = menu.menu_input_number()
                        if show_input == 0:
                            break
                        print("")
                        print("Titel:", data_list[show_input - 1]['Title'], "\nÅrtal:", data_list[show_input - 1]['Year'],
                              "\nTyp:", data_list[show_input - 1]['Type'], "\nimdb id:", data_list[show_input - 1]['imdbID'])
                        show_list.append(data_list[show_input - 1])
                        break
                    except IndexError:
                        print("Skriv endast in giltiga nummer.")
                break
            else:
                for entry in data_list:
                    print(data_list[0])
                    show_list.append(data_list[0])
                break

    def print_history(self):
        if len(history_list) > 0:
            for entry in history_list:
                print(entry)
        else:
            print("Du har ingen sökhistoria.")

    def show_information(self):
        print("")
        print("Titel:", show_list[0]['Title'], "\nÅrtal:", show_list[0]['Year'],
              "\nTyp:", show_list[0]['Type'], "\nimdb id:", show_list[0]['imdbID'])
