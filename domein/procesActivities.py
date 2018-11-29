from datetime import datetime

from database.get import select_category_by_id, select_time_by_date_endtime_cid, select_once_by_cid_and_date
from database.get import select_pot_by_categoryId
from database.insert import insert_once, insert_time_start, insert_money, insert_transaction
from database.update import update_time_end

def add_activity_by_id(userId, categoryId, amount = 0): 
            category = select_category_by_id(userId, categoryId)
            if category[4] == 1: # time
                message = proces_time(category)
            elif category[5] == 1: # money
                message = proces_money(category, amount)
            elif category[6] == 1: # once
                message = proces_once(category)
            elif category[7] == 1: # pot
                message = proces_pot(userId, category, amount)
            else :
                message = 'Error found no category'
            return message

def proces_time(category):
    date =  datetime.today().strftime('%Y-%m-%d')
    time = datetime.today().strftime('%H:%M:%S')
    if len(select_time_by_date_endtime_cid(category[0], date)) == 0:
        insert_time_start(category[0], date, time)
        message = 'start'
    else :
        update_time_end(category[0], date, time)
        message = 'end'
    return message

def proces_money(category, amount):
    date = datetime.today()
    try :
        if int(amount) > 0 : 
            insert_money(category[0], int(amount), date)
            message = 'succes_money'
        else :
            message = 'not belowe 0'
    except ValueError:
        message = 'Value Error not an Integer'
    return message

def proces_once(category):
    date =  datetime.today().strftime('%Y-%m-%d')
    if len(select_once_by_cid_and_date(category[0], date)) == 0:
        insert_once(category[0], date)
        message = 'succes_once'
    else :
        message = 'already_saved'
    return message 

def  proces_pot(userId, category, amount):
        date = datetime.today()
        pot = select_pot_by_categoryId(category[0])
        try :
            insert_transaction(pot[0], userId, amount, date)
            message = 'succes_pot'
        except ValueError :
            message = "Error"
        return message
