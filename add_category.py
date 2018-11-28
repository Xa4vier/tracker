from insert import insert_category

def add_new_category(typeNumber, name, points):
    '''typeNumber 
    1 = time
    2 = money
    3 = once '''
    try : 
        if typeNumber == 1:
            insert_category(name, True, False, False, points)
            message = 'succes'
        elif typeNumber == 2 :
            insert_category(name, False, True, False, points)
            message = 'succes'
        elif typeNumber == 3:
            insert_category(name, False, False, True, points)
            message = 'succes'
        else :
            message = 'Not a category'
    except ValueError :
        message = 'Value Error not an Integer'
    return message