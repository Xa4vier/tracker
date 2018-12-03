from database.insert import insert_category, insert_pot
from database.get import select_all_from_category_by_userId

def get_all_categories_user(userId):
    return select_all_from_category_by_userId(userId)

def add_new_category(typeNumber, name, points, userId, groupId = 0, *arg):
    '''typeNumber 
    1 = time
    2 = money
    3 = once 
    4 = pot'''
    try : 
        if typeNumber == 1:
            insert_category(name, True, False, False, False, points, userId, groupId)
            message = 'succes'
        elif typeNumber == 2 :
            insert_category(name, False, True, False, False, points, userId, groupId)
            message = 'succes'
        elif typeNumber == 3:
            insert_category(name, False, False, True, False, points, userId, groupId)
            message = 'succes'
        elif typeNumber == 4:
            categoryId = insert_category(name, False, False, False, True, points, userId, groupId)
            insert_pot(categoryId, *arg)
            message = 'succes'
        else :
            message = 'Not a category'
    except ValueError :
        message = 'Value Error not an Integer'
    return message