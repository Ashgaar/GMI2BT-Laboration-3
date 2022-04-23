import json
from movies import history_list

json_file = "movies.json"

class Json():
    def save_to_json(self):
        with open(json_file, "w", encoding="utf-8-sig") as f:
            json.dump(history_list, f)


    def read_from_json(self):
        try:
            with open(json_file,"r", encoding="utf-8-sig") as f:
                data = json.load(f)
                for entry in data:
                    history_list.append(entry)
        except ValueError:
            print("Json filen är inkorekkt formaterad. Ta gärna bort filen.")
        except FileNotFoundError:
            print("Json filen finns inte. Skapar därför en ny fil.")
            with open(json_file, "w", encoding="utf-8-sig") as f:
                json.dumps(history_list)