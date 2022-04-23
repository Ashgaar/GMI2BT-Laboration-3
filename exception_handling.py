def check_if_number():
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print("Skriv endast in nummer.")
    return value


def check_if_list_error(list):
    try:
        if list['Error']:
            print("Vi hittade inte vad du letade efter.")
            return False
        else:
            return True
    except KeyError:
        return True
