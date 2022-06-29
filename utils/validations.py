def register(field, value):
    answer = value
    # if value == "":
    while value == "":
        value = input(field.capitalize() + ": ")
    # if str(value).lower() == 'y': answer = True
    # if str(value).lower() == 'n': answer = False
    # if field == 'paid' and str(value).lower() == 'transfer' or str(value).lower() == 't':
    #     answer = "Transfer"
    # if str(value).lower() == 'i': answer = "In"
    # if str(value).lower() == 'o': answer = "Out"
        # if value != '': answer = value
    return answer
